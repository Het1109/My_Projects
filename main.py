# import requests
# from datetime import datetime
#
# MY_LATITUDES = 22.285297
# MY_LONGITUDE = 73.363808
#
#  # response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # # print(response.status_code)
# # response.raise_for_status()
# #
# # longitude = response.json()["iss_position"]["longitude"]
# # latitude = response.json()["iss_position"]["latitude"]
# #
# # iss_position = (longitude ,latitude)
# # print(iss_position)
#
# parameters = {
#     "lat" : MY_LATITUDES,
#     "lng": MY_LONGITUDE ,
#     "formatted": 0,
# }
# response = requests.get(url="https://api.sunrise-sunset.org/json" , params=parameters )
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
#
# print(sunrise)
# print( sunset)
#
# time_now = datetime.now()
# print(time_now.hour)

from datetime import datetime, timedelta
import requests

MY_LATITUDES = 22.285297
MY_LONGITUDE = 73.363808

# Parameters for API request
parameters = {
    "lat": MY_LATITUDES,
    "lng": MY_LONGITUDE,
    "formatted": 0,  # Get data in UTC
}

# Fetching sunrise and sunset data
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# Extracting sunrise and sunset times in UTC
sunrise_utc = data["results"]["sunrise"]
sunset_utc = data["results"]["sunset"]

# Converting to datetime objects
sunrise_time_utc = datetime.fromisoformat(sunrise_utc)
sunset_time_utc = datetime.fromisoformat(sunset_utc)

# Converting UTC to IST (UTC + 5:30)
ist_offset = timedelta(hours=5, minutes=30)
sunrise_time_ist = sunrise_time_utc + ist_offset
sunset_time_ist = sunset_time_utc + ist_offset

# Printing sunrise and sunset times in IST
print(f"Sunrise in IST: {sunrise_time_ist.strftime('%H:%M:%S')}")
print(f"Sunset in IST: {sunset_time_ist.strftime('%H:%M:%S')}")

# Current time in IST
time_now_utc = datetime.utcnow()
time_now_ist = time_now_utc + ist_offset
print(f"Current time in IST: {time_now_ist.strftime('%H:%M:%S')}")
