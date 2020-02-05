import os
import slack
import requests
import json
from tokeni import *

client = slack.WebClient(token=tokeni)

response2 = requests.get("http://127.0.0.1:8000/drink/?format=json")
json_data = json.loads(response2.text)
print(json_data[0].get('username'))

i = 0
for x in json_data:

    print(i)

    response = client.chat_postMessage(
        channel='#general',
        text=json_data[i].get('name')),
        
        
    response = client.chat_postMessage(
        channel='#random',
        text=json_data[i].get('name'))

    i += 1