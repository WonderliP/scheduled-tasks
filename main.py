import requests
import os
from twilio.rest import Client

MY_LAT = 46.4843023
MY_LONG = 30.7322878
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.environ.get(OWM_API_KEY)
account_sid = os.environ.get(TWILIO_ACCOUNT_SID)
auth_token = os.environ.get(TWILIO_AUTH_TOKEN)

weather_params = {
    "lat": 43.2630018,
    "lon": -2.9350039,
    "appid": API_KEY,
    "cnt": 5,
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

for time_period in weather_data["list"]:
    condition_code = time_period["weather"][0]["id"]
    if condition_code < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an ☔",
            from_="+16812271664",
            to="+380931073934",
        )
        break
