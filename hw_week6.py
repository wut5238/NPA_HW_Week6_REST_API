import requests
import urllib.parse
import json

accesstoken = "YThkODU5MDMtZDE3Mi00YWFhLWJiNDYtNTY4NzYzYWQ4YThjNGRmYTczOWItZWMz_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f"
headers = {
 'Authorization': 'Bearer {}'.format(accesstoken),
 'Content-Type': 'application/json'
}
check = input("what room? ")
def room():
    url_room = "https://webexapis.com/v1/rooms"
    json_data = requests.get(url_room, headers=headers).json()
    for i in json_data["items"]:
        if i["title"] == check:
            return i["id"]
def message():
    url_message = "https://webexapis.com/v1/messages"
    paramas = {"roomId": room(), "max":1}
    json_data = requests.get(url_message, headers=headers, params=paramas).json()
    return json_data["items"][0]["text"]

def lat_lon():
    location = message()[1:]
    print(location)
    url = "http://www.mapquestapi.com/geocoding/v1/address?"
    key = "677Aj2t5YizNv5wG7D5AGO6B5ZY2L7zS"
    url_map = url + urllib.parse.urlencode({"key":key, "location":location})
    print(url_map)
    json_data = requests.get(url_map).json()
    lat = json_data["results"][0]["locations"][0]["latLng"]["lat"]
    lon = json_data["results"][0]["locations"][0]["latLng"]["lng"]
    return [lat, lon]
# print(json.dumps(lat_lon(), indent=4))
print(lat_lon())
# while True: 
#     print(message())
#     if message().startswith("/"):
#         print("yes")
#     else:
#         print("no")