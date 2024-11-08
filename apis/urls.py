# apis/urls.py
from django.urls import path
from .views import LocationRegister,CalculateDistance

urlpatterns = [

    path('location-register/', LocationRegister.as_view()),
    path('calculate_distance/', CalculateDistance.as_view(), name='calculate_distance'),
    
]
