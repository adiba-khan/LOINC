#import relevant libraries
from urllib.request import urlopen
from urllib.parse import quote
import requests
import json

#parse input json
with open(r'patient_data.json') as f:
    my_json = json.load(f)

baseUrl = 'https://fhir.loinc.org/CodeSystem/$lookup?system=http://loinc.org&code='

#define function to access API using valid credentials
def getLOINCbyCode(LOINC):
	url = baseUrl + LOINC
	username = #'your username'
	password = #'your password'
	r = requests.get(url, auth=(username, password))
	page = r.content
	data = json.loads(page.decode('utf-8'))

	return(data['parameter'][1]['valueString'])

print(getLOINCbyCode(f'4544-3'))
