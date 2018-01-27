import requests
from pprint import pprint
import os

DOXIE_IP = 'http://192.168.1.40:8080/'


helloResponse = requests.get(DOXIE_IP + 'hello.json')
helloExtraResponse = requests.get(DOXIE_IP + 'hello_extra.json')

jsonHelloResponse = helloResponse.json()

if helloExtraResponse.json()['connectedToExternalPower']:
    powerResponse = "connected."
else:
    powerResponse = "not connected."

print(jsonHelloResponse['name'] + " with ip " + jsonHelloResponse['ip'] +
      " is connected to network " + jsonHelloResponse['network'] + ", " +
      powerResponse)

print("Listing existing scans…")

scansResponse = requests.get(DOXIE_IP + 'scans.json')

for scan in scansResponse.json():
    print("Downloading " + os.path.basename(scan['name']))

    downloadResponse = requests.get(
        DOXIE_IP + 'scans' + scan['name'], stream=True)

    with open(os.path.basename(scan['name']), 'wb') as saveLocation:
        for chunk in downloadResponse.iter_content(chunk_size=128):
            saveLocation.write(chunk)
