from apps.accounts.models import Geoposition

from base.integrations import get_geoposition


def get_or_create_location_instance(city_name: str) -> Geoposition:
    geopositions = get_geoposition(query=city_name)
    return Geoposition.objects.get_or_create(**geopositions.__dict__)[0]
