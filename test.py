import requests
import json

# / == %2F

url = "http://0.0.0.0:9001/repos"

with open("test_json.json") as f:
    data = json.load(f)

resp = requests.post(url, json=data)
print(resp)
