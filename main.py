import requests
from twilio.rest import Client

END_POINT = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "Your_api_key"
account_sid = "Your_Account_sid"
auth_token = "Your_auth_token"
MY_LAT = 50.234612
MY_LON = -3.769470

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": api_key,
    "exclude": "current, minutely, daily"
}
response = requests.get(END_POINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_weather = [weather_data["hourly"][hour]["weather"][0]["id"] for hour in range(0, 12) if weather_data["hourly"][hour]["weather"][0]["id"] < 600]
if hourly_weather:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔",
            from_='+447777777776',
            to='+447777777777'
        )
    print(message.status)




