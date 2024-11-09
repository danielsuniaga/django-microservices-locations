# apis/urls.py
from django.urls import path
from .views import LocationRegister,CalculateDistance,GetTaskStatus

urlpatterns = [

    path('location-register/', LocationRegister.as_view()),

    path('calculate_distance/', CalculateDistance.as_view(), name='calculate_distance'),
    
    path('task_status/<str:task_id>/', GetTaskStatus.as_view(), name='task_status'),
    
]
