from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_forecast_view, name='weather_forecast'),  # This makes /weather/ go to your weather page.
]
