import requests
from pprint import pprint

response = requests.get('http://192.168.1.40:8080/scans/recent.json')

pprint(response.json())
