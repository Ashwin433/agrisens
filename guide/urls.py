from django.urls import path
from . import views

urlpatterns = [
    path('', views.smart_farming_guide, name='smart_farming_guide'),
]
