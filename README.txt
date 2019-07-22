This modular input can retrieve data from Paessler PRTG Network Monitor. The PRTG API is excellent and provides access to almost all data. The typical use case is to periodically retrieve sensor status and values. 

The recommended format for retreiving data is the JSON format, and this should work correctly with minimal customisation. If you want to use other data formats then you will need to create Splunk parsing properties and possibly field extractions etc.

In PRTG, naviagate to `Setup` > `API` for documentation as well as a query builder that is useful for constructing a URL that can be used in this modular input. The documention in the PRTG UI easiest to read, but online API documentation is also available online: https://www.paessler.com/manuals/prtg/application_programming_interface_api_definition 

[Splunkbase](https://splunkbase.splunk.com/app/4610/#/details) | [Source code](https://github.com/ChrisYounger/TA-prtg-input) |  [Questions, Bugs or Suggestions](https://answers.splunk.com/app/questions/4610.html) | [My Splunk apps](https://splunkbase.splunk.com/apps/#/author/chrisyoungerjds)



## Examples:

Retreiving all sensors:
`/api/table.json?content=sensors&output=json&columns=objid,probe,group,device,sensor,status,message,lastvalue,priority&count=1000`

Retreving specific sensor (includes child sensors):
`/api/table.json?content=sensors&output=json&id=2003&columns=objid,probe,group,device,sensor,status,message,lastvalue,priority&count=1000`

Retreving all sensors in warning or alarm status:
`/api/table.json?content=sensors&count=1000&output=json&columns=objid,probegroupdevice,device,sensor,status,lastvalue,message,priority&sortby=priority&filter_status=4&filter_status=5&filter_status=10&filter_status=13&filter_status=14`



