import requests
import urllib.parse
import json

accesstoken = "OWFkNmM2YmEtYzM2MC00ZDQ4LWI4NDUtNmM5ZDQxYmVhYzA3MGYwZGY5MzAtMTNj_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f"
headers = {
 'Authorization': 'Bearer {}'.format(accesstoken),
 'Content-Type': 'application/json'
}
check = input("what room? ")
def room():
    url_room = "https://webexapis.com/v1/rooms"
    json_data = requests.get(url_room, headers=headers).json()
    # print(json_data)
    for i in json_data["items"]:
        if i["title"] == check:
            return i["id"]
def message():
    url_message = "https://webexapis.com/v1/messages"
    paramas = {"roomId": room(), "max":1}
    json_data = requests.get(url_message, headers=headers, params=paramas).json()
    print(json_data["items"][0]["text"])

while True:
    message()
