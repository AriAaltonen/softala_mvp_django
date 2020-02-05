import os
import slack
import requests
import json


client = slack.WebClient(token="xoxb-920314795317-920300349808-SIFPPJ9fftwuD4ZwSnzMoMrE")

response2 = requests.get("http://127.0.0.1:8000/drink/?format=json")
json_data = json.loads(response2.text)





print(json_data[0].get('username'))


i = 0
for x in json_data:

    print(i)
    response = client.chat_postMessage(
        channel='#testibot',
        text=json_data[i].get('name')),


    response = client.chat_postMessage(

        channel='#random',
        text=json_data[i].get('name'))
    i += 1





