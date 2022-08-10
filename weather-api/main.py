import requests

API_KEY = '389c82bf0ad6f18c71141214f1154e77'
CITY = 'London'
API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'
IMAGE_API_KEY = '29188269-b83105c6bfe5ac1814d3944bb'

response = requests.get(API_URL)
response_json = response.json()
sky_mode = response_json["weather"][0]["main"]

IMAGE_API_URL = f'https://pixabay.com/api/?key={IMAGE_API_KEY}&q={sky_mode}&image_type=photo'

image_response = requests.get(IMAGE_API_URL)

#print(image_response.json())


