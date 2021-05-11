import requests
import json

# / == %2F

url = "https://my-new-app-denini.herokuapp.com/repos"

with open("test_json.json") as f:
    data = json.load(f)

resp = requests.post(url, json=data)
print(resp)
