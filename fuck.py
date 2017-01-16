# -*- coding: utf-8 -*-
import sys, urllib, urllib.request, json

# city = urllib.quote(sys.argv[1])
city = "北京"

url = 'http://apis.baidu.com/xiaota/bus_lines/buses_lines?city=%s&bus=%s&direction=%s'%(city,sys.argv[2],sys.argv[3])

print (url)

req = urllib.request.Request(url)

req.add_header("apikey", "2f5da4b87cbd02a5f8be1189db99b6a8")

resp = urllib.request.urlopen(req)
content = resp.read()
if(content):
    print(content)

print ("\n")
busStation = json.loads(content)
print (busStation.keys())
print (busStation['data'].keys())
print (busStation['data']['stations'])


for bus in busStation['data']['stations']:
        print (bus['stateName'])