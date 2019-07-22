[prtg_input://<name>]
url_path_of_api = E.g. /api/table.json?content=sensors&output=json&count=1000&columns=objid,probe,group,device,sensor,status,message,priority
split_json_arrays = 
custom_sourcetype = Sourcetype "prtg:json" is a good default for output=json queries with "Split JSON arrays" enabled. If using other PRTG output methods you will need to create parsing props yourself.