from rest_framework import serializers

from apps.accounts.models import Geoposition, User


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geoposition
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer()

    class Meta:
        model = User
        fields = ('username', 'location')
