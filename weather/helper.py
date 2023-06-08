import requests
import json
from private.keys import WEATHER_KEY


class Weather:

    def __init__(self):
        self._url = 'https://api.openweathermap.org/data/2.5/weather?'  # open weather base url
        self.response = None
        self.data = None

    def set_data(self, city):
        params = {
            'q': city,
            'appid': WEATHER_KEY,
            'units': 'metrics'
        }
        self.response = requests.get(self._url, params)
        response = self.response
        self.data = json.loads(response.text)

    def get_data(self):
        return self.data

    def is_success(self):
        return self.response.status_code == 200

    def get_temp(self):
        return round(self.data['main']['temp'] - 273.15, 2)

    def get_dsc(self):
        return self.data['weather'][0]['description']

    def get_main(self):
        return self.data['weather'][0]['main']

    def get_humidity(self):
        return self.data['main']['humidity']

    def get_icon(self):
        icon_id = self.data['weather'][0]['icon']
        return f'http://openweathermap.org/img/wn/{icon_id}@2x.png'


def get_weather(city):
    weather = Weather()
    weather.set_data(city)
    if weather.is_success():
        return f'The weather in {city} is like {weather.get_main()} with temperature is {weather.get_temp()}°C and humidity is {weather.get_humidity()}'
    return "I can't able to fetch the weather information. I think the city name is wrong"
