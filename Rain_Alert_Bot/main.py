
# from twilio.rest import Client
import requests
from credentials import *
OWN_Endpoint = OWN_Endpoint
api_key = api_key
account_sid = account_sid
auth_token = auth_token

# # Srinagar data
# weather_params = {
#     "lat" : 34.083672 , "lon" : 74.797279,
#     "appid" : api_key ,
#     "cnt" : 4,
#     }


# Jakarta data
weather_params = {
    "lat" :-6.175110 ,
    "lon" : 106.865036,
    "appid" : api_key ,
    "cnt" : 4,
    }

response = requests.get(OWN_Endpoint  , params = weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

Baarish_hogi = False

for hour in weather_data["list"]:
    condition = hour["weather"][0]["id"]
    # print(condition)
    if int(condition) < 700:
        Baarish_hogi = True

if Baarish_hogi:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Umbrella le lena bhai Baarish ho rahi heh.☔🌧️",
    from_="+12319362944",
    to="+919824134706",  )
    print(message.status)
