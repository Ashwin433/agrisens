from django.urls import path
from . import views

urlpatterns = [
    path('recommend/', views.crop_recommendation_view, name='crop_recommendation'),
]
