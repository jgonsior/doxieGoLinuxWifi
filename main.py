#!/usr/bin/python3
import requests
import os
import configparser
from pprint import pprint
from xdg import XDG_CONFIG_HOME

cfgDir = XDG_CONFIG_HOME + "/doxieGoLinuxWifi/"
cfg = configparser.ConfigParser()
cfg.read(cfgDir + "config")
# first get some status information from the doxie
try:
    helloResponse = requests.get(cfg['DEFAULT']['doxieIp'] + 'hello.json')
except requests.exceptions.ConnectionError as e:
    print("Unable to connect to " + cfg['DEFAULT']['doxieIp'] +
          ". Are you sure your Doxie is correctly connected to a wifi?")
    exit()

helloExtraResponse = requests.get(
    cfg['DEFAULT']['doxieIp'] + 'hello_extra.json')

jsonHelloResponse = helloResponse.json()

if helloExtraResponse.json()['connectedToExternalPower']:
    powerResponse = "connected."
else:
    powerResponse = "not connected."

print(jsonHelloResponse['name'] + " with ip " + jsonHelloResponse['ip'] +
      " is connected to network " + jsonHelloResponse['network'] + ", " +
      powerResponse)

# download new scans

print("Checking for new scans…")

recentResponse = requests.get(
    cfg['DEFAULT']['doxieIp'] + 'scans/recent.json')

# make sure the "recent" file exists
if not os.path.isfile(cfgDir + "recent"):
    open(cfgDir + "recent", "a").close()

with open(cfgDir + "recent", "r") as f:
    recentFile = f.readline()


if recentResponse.json()['path'] == recentFile:
    print("No new files today.")
else:
    with open(cfgDir + "recent", "w") as f:
        f.write(recentResponse.json()['path'])

    scansResponse = requests.get(cfg['DEFAULT']['doxieIp'] + 'scans.json')

    for scan in scansResponse.json():
        print("Found ")

        saveLocation = os.path.basename(scan['name'])
        print("Downloading " + saveLocation)

        downloadResponse = requests.get(
            cfg['DEFAULT']['doxieIp'] + 'scans' + scan['name'], stream=True)

        with open(saveLocation, "wb") as f:
            for chunk in downloadResponse.iter_content(chunk_size=128):
                f.write(chunk)

            # color: -rgb -unpo "-no-blurfilter"
            # b/w: -resolution 450
