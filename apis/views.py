# Django imports
from django.shortcuts import render
from django.db import connection

# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Location
from .serializers import LocationSerializer

from math import sqrt

def calculate_distance(point1, point2):
    lat1, lon1 = point1
    lat2, lon2 = point2
    return sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)

class CalculateDistance(APIView):
    def post(self, request, *args, **kwargs):
        # Obtener la lista de IDs de ubicaciones desde la solicitud
        location_ids = request.data.get('location_ids', [])
        
        # Validar que la lista de IDs no esté vacía
        if len(location_ids) < 2:
            return Response({'error': 'Debe haber al menos dos ubicaciones'}, status=status.HTTP_400_BAD_REQUEST)

        # Obtener las ubicaciones correspondientes a los IDs
        locations = Location.objects.filter(id__in=location_ids)
        
        # Verificar que todas las ubicaciones fueron encontradas
        if len(locations) != len(location_ids):
            return Response({'error': 'Algunas ubicaciones no fueron encontradas'}, status=status.HTTP_404_NOT_FOUND)
        
        # Calcular la distancia total entre las ubicaciones
        total_distance = 0
        for i in range(len(locations) - 1):
            point1 = (locations[i].latitude, locations[i].longitude)
            point2 = (locations[i + 1].latitude, locations[i + 1].longitude)
            total_distance += calculate_distance(point1, point2)

        # Retornar la distancia total
        return Response({'total_distance': total_distance}, status=status.HTTP_200_OK)

class LocationRegister(APIView):

    def post(self, request, *args, **kwargs):

        serializer = LocationSerializer(data=request.data)

        if serializer.is_valid():

            location = serializer.save()

            return Response({"id": location.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
