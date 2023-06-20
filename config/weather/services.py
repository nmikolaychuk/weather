import requests
import datetime

from typing import NamedTuple

from django.conf import settings
from .exceptions import GetWeatherError


Celsius = float
IconCode = str


class WeatherInfo(NamedTuple):
    """Информация о погоде."""
    city: str
    temperature: Celsius
    description: str
    sunrise: datetime.datetime
    sunset: datetime.datetime
    icon: IconCode


def get_weather_by_city_name(city_name: str) -> WeatherInfo:
    """Получить информацию о погоде для указанного города."""
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather' \
              f'?q={city_name}&appid={settings.OPEN_WEATHER_API_TOKEN}&units=metric'
        response = requests.get(url).json()

        return WeatherInfo(
            city=city_name,
            temperature=response['main']['temp'],
            description=response['weather'][0]['description'],
            sunrise=datetime.datetime.fromtimestamp(response['sys']['sunrise']),
            sunset=datetime.datetime.fromtimestamp(response['sys']['sunset']),
            icon=response['weather'][0]['icon'],
        )
    except KeyError:
        raise GetWeatherError
