import requests
import urllib.parse
import json
from datetime import datetime

country = input("Enter country which you want (plese enter full name) : ").lower()
url_ls_country = "https://restcountries.eu/rest/v2/all"
json_data_lsc = requests.get(url_ls_country).json()

for i in range(len(json_data_lsc)):
    # print(country, json_data_lsc[i]["name"].lower())
    if country == json_data_lsc[i]["name"].lower():
        url_currency_code = "https://restcountries.eu/rest/v2/name/"+country
        json_data_cc = requests.get(url_currency_code).json()
        currency = json_data_cc[0]["currencies"][0]["code"]
        print("currency code of {} is".format(json_data_lsc[i]["name"]), currency)

        url_rates = "https://api.exchangerate-api.com/v4/latest/USD"
        json_data_r = requests.get(url_rates).json()
        beauty_json = json.dumps(json_data_r["rates"][currency], indent=4)
        print("Exchange rate from USD to {} now is".format(currency), beauty_json)
        print("Last update is : {}".format(datetime.fromtimestamp(json_data_r["time_last_updated"])))
        break
    elif i == len(json_data_lsc)-1:
        print("It's not Country")
    else:
        continue
        
