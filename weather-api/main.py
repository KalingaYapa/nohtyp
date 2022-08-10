import requests

API_KEY = '389c82bf0ad6f18c71141214f1154e77'
CITY = 'London'
API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'

response = requests.get(API_URL)
response_json = response.json()
sky_mode = response_json["weather"][0]["main"]

print(sky_mode)


