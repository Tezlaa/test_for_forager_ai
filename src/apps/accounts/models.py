from django.db import models
from django.contrib.auth.models import AbstractUser


class Geoposition(models.Model):
    """
    Added latitude and longitude for user city.
    """

    name = models.CharField(max_length=164, verbose_name='name')
    country = models.CharField(max_length=5, verbose_name='cuntry')
    lat = models.FloatField(verbose_name='city latitude')
    lon = models.FloatField(verbose_name='city longitude')


class User(AbstractUser):
    """
    Castomize Django user. Added location fields.
    """
    city_name = models.CharField(max_length=164, verbose_name='City name')
    location = models.ForeignKey(to=Geoposition, on_delete=models.CASCADE, blank=True, null=True)
