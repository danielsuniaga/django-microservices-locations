# tasks.py
from celery import shared_task
from math import sqrt
from .models import Location

@shared_task
def calcular_distancia(location_ids):

    locations = Location.objects.filter(id__in=location_ids)
    
    if len(locations) != len(location_ids):
        return {'error': 'Algunas ubicaciones no fueron encontradas'}

    total_distance = 0
    for i in range(len(locations) - 1):
        point1 = (locations[i].latitude, locations[i].longitude)
        point2 = (locations[i + 1].latitude, locations[i + 1].longitude)
        total_distance += sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

    return {'total_distance': total_distance}
