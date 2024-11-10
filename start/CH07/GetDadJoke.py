import requests

url = "https://icanhazdadjoke.com/"
headers = {"Accept": "application/json"}

response = requests.get(headers=headers, url=url)

response_data = response.json()

print(response_data['joke'])

