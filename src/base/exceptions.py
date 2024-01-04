from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import APIException
from rest_framework import status


class CityNotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = _('No place with that name was found! Try again')


class InvalidAPIKey(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = _('Invalid API key.')


class ReceiptError(APIException):
    status_code = status.HTTP_502_BAD_GATEWAY
    default_code = _('Receipt error. Try again!')
