import requests
import json

url = "https://api.restful-api.dev/objects/1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

with open("data/response.json", "w") as file:
    json.dump(json.loads(response.text), file, indent=4)

print("JSON saved to 'data/response.json'")
rint("JSON saved to 'data/response.json from branch'")

