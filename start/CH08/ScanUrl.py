import requests
import json

#Will be chaning this API key after assignment is graded.
api_key = 'api_key'

url = input("Enter a URL to scan\n")

headers = {'API-Key':api_key,'Content-Type':'application/json'}
data = {"url": url, "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
print(response)
print(response.json().get('result'))