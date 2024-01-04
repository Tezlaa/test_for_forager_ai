import json

from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from apps.accounts.models import User
from apps.accounts.services.location import get_or_create_location_instance


class TestWeatherViews(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.test_data = {
            'username': 'UserTest',
            'password': 'testPass',
            'city_name': 'Kyiv',
            'location': get_or_create_location_instance('Kyiv')
        }
        self.test_client = User.objects.create(**self.test_data)
        self.client.force_authenticate(self.test_client)

    def test_current_weather_api(self):
        response = self.client.get(reverse('current-weather'))
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json.get('coord').get('lon'), 30.525)
        self.assertEqual(response_json.get('coord').get('lat'), 50.4494)
        self.assertEqual(response_json.get('user').get('username'), 'UserTest')

    def test_search_weather_api(self):
        response = self.client.get(reverse('search-by-direct', args=['Kyiv']))
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json.get('coord').get('lon'), 30.525)
        self.assertEqual(response_json.get('coord').get('lat'), 50.4494)

        response = self.client.get(reverse('search-by-direct', args=['56']))
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json.get('coord').get('lon'), 16.0809)
        self.assertEqual(response_json.get('coord').get('lat'), 46.8349)

    def test_forecast_weather_api(self):
        response = self.client.get(reverse('forecast-weather'))
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json.get('city').get('coord').get('lon'), 30.5241)
        self.assertEqual(response_json.get('city').get('coord').get('lat'), 50.45)
        self.assertEqual(response_json.get('user').get('username'), 'UserTest')

        response = self.client.get(reverse('forecast-weather'), data={'city_name': 'Dnepr'})
        response_json = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_json.get('city').get('coord').get('lon'), 35.0418)
        self.assertEqual(response_json.get('city').get('coord').get('lat'), 48.468)
        self.assertEqual(response_json.get('user').get('username'), 'UserTest')
