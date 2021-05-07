import requests
import json

# / == %2F

url = "http://localhost:3000/runs"

with open("test_json.json") as f:
    data = json.load(f)

requests.post(url, json=data)
