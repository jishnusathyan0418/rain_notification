import requests
from twilio.rest import Client

account_sid = 'ACfeaad9a71c7a89431147f784a9710fe2'
auth_token = '7d967d4dc6d730c890e0f8a3e52f5f59'



end_point = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "23281518820da1d7988f419af1ba8e9b"
bring_umberlla = False

parameter = {
    "lat": 13.082680,
    # "lat": 10.6139,
    "lon": 80.270721,
    # "lon": 76.6908,
    "appid": api_key,
    "cnt": 4
}
responce = requests.get(end_point, params=parameter)
responce.raise_for_status()
weather_data = responce.json()
for hour_data in weather_data['list']:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) <= 500:
        bring_umberlla = True
if bring_umberlla:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = 'It is about to to rain.Remainder to take an umbrella!',
        from_='+15737314766',
        to='+918547333849'
    )
    print(message.status)
