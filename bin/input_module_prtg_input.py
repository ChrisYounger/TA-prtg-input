encoding = "utf-8"

import os, sys, time, json, datetime, requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def validate_input(helper, definition):
    pass

def collect_events(helper, ew):
    helper.set_log_level(helper.get_log_level())

    username = helper.get_global_setting("username")
    password = helper.get_global_setting("password")
    passhash = helper.get_global_setting("passhash")
    base_url = helper.get_global_setting("base_url")
    url_stem = helper.get_arg('url_path_of_api')
    splitjson = helper.get_arg('split_json_arrays')
    custom_sourcetype = helper.get_arg('custom_sourcetype')
    
    if username == None:
        username = ""
    if password == None:
        password = ""
    if passhash == None:
        passhash = ""
    if base_url == None:
        base_url = ""
    if url_stem == None:
        url_stem = ""
    if custom_sourcetype == None:
        custom_sourcetype = ""
        
    username = username.strip()
    password = password.strip()
    passhash = passhash.strip()
    base_url = base_url.strip()
    url_stem = url_stem.strip()
    
    if not url_stem.startswith('/'):
        url_stem = "/" + url_stem
    if base_url.endswith('/'):
        base_url = base_url[:-1]
        
    url = base_url + url_stem
    params = {
        "username": username,
    }
    if password != "":
        params["password"] = password
    else:
        params["passhash"] = passhash
    
    data = ""
    
    proxy_settings = helper.get_proxy()

    helper.log_info("Requesting URL: " + url + " with username=" + username)

    # The following examples send rest requests to some endpoint.
    response = helper.send_http_request(url, "GET", parameters=params, payload=None,
                                        headers=None, cookies=None, verify=False, cert=None,
                                        timeout=30, use_proxy=True)
                                        
    # If the body text is not a json string, raise a ValueError
    handled = False
    if splitjson:
        try:
            r_json = response.json()
            for key in r_json:
                if isinstance(r_json[key], list):
                    for item in r_json[key]:
                        data += json.dumps(item) + "\n"
            handled = True
        except ValueError:
            # ignore
            data += ""
            
    if not handled:
        data += str(response.text)
    
    sourcetype = helper.get_sourcetype()
    if custom_sourcetype != "":
        sourcetype = custom_sourcetype

    event = helper.new_event(source=helper.get_input_stanza_names(), index=helper.get_output_index(), sourcetype=sourcetype, data=data)
    
    ew.write_event(event)
