# apis/urls.py
from django.urls import path
from .views import LocationRegister

urlpatterns = [

    path('location-register/', LocationRegister.as_view())
    
]
