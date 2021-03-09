import requests
import urllib.parse
import json

accesstoken = "OWFkNmM2YmEtYzM2MC00ZDQ4LWI4NDUtNmM5ZDQxYmVhYzA3MGYwZGY5MzAtMTNj_P0A1_408b8cf5-9f52-48d9-be13-2cd9891ab13f"
url = "https://webexapis.com/v1/rooms"

headers = {
 'Authorization': 'Bearer {}'.format(accesstoken)
}

json_data = requests.get(url, headers=headers).json()
print(json.dumps(json_data, indent=4))
