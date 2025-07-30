import requests

url = "https://api.restful-api.dev/objects/1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
