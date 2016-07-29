#!/usr/bin/python
# title : thingxpi.py
# author: Daniel Nissenbaum
#
# This is a Python script to gather readings on the Raspberry Pi and connected
# sensors and update the properties for a 'thing' on a ThingWorx instance.
#
# This particular script gets data from a connected OBD2 port
#
# From the command line run,
# './thingxpi.py <thing> <ThingWorx url> <Application Key>
#
#


import requests
import sys
import json
import time
import subprocess
import obd_thing_capture as obd_data

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings()

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Info to connect to Thingworx
thing = sys.argv[1]
url = sys.argv[2]
appKey = sys.argv[3]

# Header data
headers = {'Content-Type': 'application/json', 'appKey': appKey}

# set up OBD capturing
logitems = ["rpm", "speed", "throttle_pos", "load", "fuel_status"]
o = obd_data.OBD_Recorder(logitems)
o.connect()

if not o.is_connected():
    print "Not connected"
# o.get_data()

while True:

    payload = o.get_data()

    for key in payload:
    	if isinstance(payload[key], float):
    		#temp = "{:.9f}".format(numvar)
    		payload[key] = round(payload[key],2) 

    print payload

    response = requests.put(url + '/Things/' + thing + '/Properties/*',
                            headers=headers, json=payload, verify=False)

    print response

    time.sleep(1)
    print '========================='
    
