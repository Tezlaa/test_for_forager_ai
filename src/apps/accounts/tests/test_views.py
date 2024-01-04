from rest_framework.test import APITestCase, APIClient

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

    def test_location_user_instance(self):
        if self.test_client.location is not None:
            self.assertEqual(self.test_client.location.name, 'Kyiv')
            self.assertEqual(self.test_client.location.lat, 50.4500336)
            self.assertEqual(self.test_client.location.lon, 30.5241361)
        else:
            raise self.failureException('Location instance is None')
