import requests
from pprint import pprint

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

response = requests.get(DOXIE_IP + 'scans/recent.json')

pprint(response.json())
