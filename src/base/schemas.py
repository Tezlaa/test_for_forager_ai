from dataclasses import dataclass


@dataclass
class GeopositionResponse:
    name: str
    country: str
    lat: float
    lon: float
