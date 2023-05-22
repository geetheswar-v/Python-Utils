import requests
import json
from constants.Keys import WEATHER_KEY

class Weather(object):
	"""Weather helper class:
		retrive the weather data of specified city"""


	def __init__(self):
		super(Weather, self).__init__()
		self.base_url = 'https://api.openweathermap.org/data/2.5/weather'
		self.api_key = WEATHER_KEY

	def set_data(self, city_name):
		params = {
		'q' = city_name,
		'appid' = self.api_key,
		'units' = 'metric'
		}
		self.response = requests.get(self.base_url, params=params)
		self.data = json.loads(response.text)


	def get_temp(self, city_name):
		set_data(self, city_name)
		if self.response.status_code == 200:
			return f'Temperature in {city_name} is {self.data['main']['temp']}'

	def get_desc(self, city_name):
		set_data(self, city_name)
		if self.response.status_code == 200:
			return f'Weather in {city_name} is {self.data['weather'][0]['description']}'


		