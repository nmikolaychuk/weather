from django.shortcuts import render

from .services import get_weather_by_city_name
from .exceptions import GetWeatherError


def get_weather(request):
    if request.method == "POST":
        city = request.POST['input_city_name']
        context = {}
        try:
            context["city_weather"] = get_weather_by_city_name(city_name=city)
        except GetWeatherError:
            pass

        return render(request=request, template_name='weather/index.html', context=context)
