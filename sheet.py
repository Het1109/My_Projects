import requests
from datetime import datetime
import pytz

APP_ID = "2159ce5e"
API_KEY = "6f697a077d378868c52a08ae5c804b87"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = "https://api.sheety.co/2b2a8ab520d39bf999fa24c9073bea57/het'sWorkoutPlan/workouts"

# My details
GENDER = "male"
WEIGHT_KG = 58
HEIGHT_CM = 173
AGE = 20

exercise_text = input("Tell me which exercise you did: ")

user_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

response1 = requests.post(url=EXERCISE_ENDPOINT, json=user_parameters, headers=headers)
result = response1.json()

# As the servers are in UTC time zone we have to
#  convert it to IST for INDIAN Time
utc_now = datetime.utcnow()
ist_timezone = pytz.timezone("Asia/Kolkata")
ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(ist_timezone)

#  Correct IST Time
India_date = ist_now.strftime("%d/%m/%Y")
India_time = ist_now.strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": India_date,
            "time": India_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_headers = {
        "Content-Type": "application/json",
        "Authorization":  "Basic bnVsbDpudWxs"
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers=sheety_headers)
    print(sheet_response.text)


# 2nd approach if u get error from above
    # sheet_response = requests.post(
    # SHEET_ENDPOINT,
    # json=sheet_inputs,
    # auth=("hetpatel", "Hello@123" )
    # )
