from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.accounts.serializers import UserSerializer

from base.integrations import (
    get_geoposition, get_forecast, get_current_weather
)


class CurrentWeather(GenericAPIView):
    """
    API for getting current weather by user location.
    Response:
        https://openweathermap.org/current#docs-list
        + 'user': {
            'username': ...,
            'location': {
                'name': ...,
                'country': ...,
                'lat': Latitude of the location,
                'lon': Longitude of the location,
            }
        }
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get(self, request) -> Response:
        user_data = self.get_serializer(request.user).data
        response = get_current_weather(geo=request.user.location)
        response['user'] = user_data

        return Response(response)


class Search(APIView):
    """
    API to search for current weather by city name or zip code:
    Response:
        https://openweathermap.org/current#docs-list
    """
    permission_classes = (IsAuthenticated, )

    def get(self, request, query: str) -> Response:
        location = get_geoposition(query=query)
        response = get_current_weather(geo=location)

        return Response(response)


class ForecastWeather(GenericAPIView):
    """
    API for getting forecast weather by user`s location or by get parameter 'city_name'.
    Response:
        https://openweathermap.org/forecast5#docs-list
        + 'user': {
            'username': ...,
            'location': {
                'name': ...,
                'country': ...,
                'lat': Latitude of the location,
                'lon': Longitude of the location,
            }
        }
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = UserSerializer

    def get(self, request) -> Response:
        user_data = self.get_serializer(request.user).data

        city_name = request.GET.get('city_name')
        if city_name:
            location = get_geoposition(query=city_name)
        else:
            location = request.user.location

        response = get_forecast(geo=location)
        response['user'] = user_data

        return Response(response)
