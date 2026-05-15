import requests
from twilio.rest import Client

MY_LAT = 46.4843023
MY_LONG = 30.7322878
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "bf91537404e25d60057450dd24f7b37a"
account_sid = "ACb5a53c594783659023cf6fb230318b5e"
auth_token = "151650df20b625b7f539751f48dc2ee6"

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
