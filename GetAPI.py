import requests

url = "https://api.restful-api.dev/objects/1"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

with open("response.json", "w") as file:
    json.dump(json_response, file, indent=4)

print("JSON saved to 'data/response.json'")

