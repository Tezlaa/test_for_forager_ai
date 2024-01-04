import requests
from requests import Response

from django.conf import settings

from base.exceptions import InvalidAPIKey, ReceiptError
from base.schemas import GeopositionResponse


def request_api(url) -> Response:
    token = settings.OPEN_WEATHER_TOKEN
    response = requests.get(url=f'{url}&appid={token}')

    valid_responce(response)
    return response


def valid_responce(response: Response) -> None | Exception:
    if response.status_code == 200:
        return
    elif response.status_code == 401:
        raise InvalidAPIKey
    else:
        raise ReceiptError


def get_geoposition(query: str) -> GeopositionResponse:
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=1'
    response = request_api(url)

    response_json = response.json()[0]

    return GeopositionResponse(
        name=response_json.get('name'),
        country=response_json.get('country'),
        lat=float(response_json.get('lat')),
        lon=float(response_json.get('lon')),
    )


def get_forecast(geo: GeopositionResponse) -> dict:
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={geo.lat}&lon={geo.lon}'
    response = request_api(url)

    return response.json()


def get_current_weather(geo: GeopositionResponse) -> dict:
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={geo.lat}&lon={geo.lon}'
    response = request_api(url)

    return response.json()
