import requests
import json
from chatmate.constants.keys import WEATHER_KEY


class Weather:

    def __init__(self):
        self._city = 'london'  # base city
        self._url = 'https://api.openweathermap.org/data/2.5/weather?'  # open weather base url
        self._params = {
            'q': self._city,
            'appid': WEATHER_KEY,
            'units': 'metrics'
        }

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city_name):
        self._city = city_name

    def get_response(self):
        return requests.get(self._url, self._params)

    def get_data(self):
        response = self.get_response()
        return json.loads(response.text)

    def is_success(self):
        return self.get_response().status_code == 200

    def get_coord(self):
        if self.is_success():
            return self.get_data()['coord']['lon'], self.get_data()['coord']['lat']

    def get_temp(self):
        if self.is_success():
            return self.get_data()['main']['temp']

    def get_dsc(self):
        if self.is_success():
            return self.get_data()['weather']['description']

    def get_feel_temp(self):
        if self.is_success():
            return self.get_data()['main']['feels_like']

    def get_humidity(self):
        if self.get_data():
            return self.get_data()['main']['humidity']
