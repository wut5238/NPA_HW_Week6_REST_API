import requests
import urllib.parse
import json
from datetime import datetime

accesstoken = "YTZhODNhNzMtOTUxZi00YjJhLThmYTQtYjA3NWY5NDk1NzM1ZWVkNjg2NDAtNGU4_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f"
headers = {
 'Authorization': 'Bearer {}'.format(accesstoken),
 'Content-Type': 'application/json'
}

def ls_room():
    url_list_room = "https://webexapis.com/v1/rooms"
    json_data = requests.get(url_list_room, headers=headers).json()
    print("list of rooms:")
    for i in json_data["items"]:
        print("-", i["title"])
ls_room()

check = input("what room? ")
def room():
    url_room = "https://webexapis.com/v1/rooms"
    json_data = requests.get(url_room, headers=headers).json()
    for i in json_data["items"]:
        if i["title"] == check:
            return i["id"]

def messages():
    url_message = "https://webexapis.com/v1/messages"
    params = {"roomId": room(), "max":1}
    json_data = requests.get(url_message, headers=headers, params=params).json()
    return json_data["items"][0]["text"]

def lat_lon():
    location = messages()[1:]
    # print(location)
    url = "http://www.mapquestapi.com/geocoding/v1/address?"
    key = ""#ไปเอา key จาก https://developer.mapquest.com/
    url_map = url + urllib.parse.urlencode({"key":key, "location":location})
    # print(url_map)
    json_data = requests.get(url_map).json()
    lat = json_data["results"][0]["locations"][0]["latLng"]["lat"]
    lon = json_data["results"][0]["locations"][0]["latLng"]["lng"]
    return [lat, lon]
# print(json.dumps(lat_lon(), indent=4))

def iss():
    lat = lat_lon()[0]
    lon = lat_lon()[1]
    url = "http://api.open-notify.org/iss-pass.json?"
    url_iss = url + urllib.parse.urlencode({"lat":lat, "lon":lon})
    json_data = requests.get(url_iss).json()
    # print(json.dumps(json_data, indent=4))
    duration = json_data["response"][0]["duration"]
    timestamp = json_data["response"][0]["risetime"]
    date_time = datetime.fromtimestamp(timestamp)
    return [duration, date_time]

def post_message():
    url = "https://webexapis.com/v1/messages"
    message = "In {} ISS will fly over on {} for {} seconds".format(messages()[1:], str(iss()[1]), str(iss()[0]))
    params = {"roomId": room(), "markdown": message}
    requests.post(url, headers=headers, json=params)
    # print(res.json())

while True:
    if messages().startswith("/"):
        post_message()
    else:
        print(messages())
