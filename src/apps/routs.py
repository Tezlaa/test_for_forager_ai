from django.urls import path, include


urlpatterns = [
    path('v1/weather/', include('apps.weather.urls'))
]
