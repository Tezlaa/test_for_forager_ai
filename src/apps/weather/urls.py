from django.urls import path

from apps.weather.views import CurrentWeather, Search, ForecastWeather


urlpatterns = [
    path('current/', CurrentWeather.as_view(), name='current-weather'),
    path('search/<str:query>', Search.as_view(), name='search-by-direct'),
    path('forecast/', ForecastWeather.as_view(), name='forecast-weather'),
]
