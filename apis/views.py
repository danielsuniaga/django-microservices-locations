# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .task import calcular_distancia

from .models import Location
from .serializers import LocationSerializer
from celery.result import AsyncResult


class CalculateDistance(APIView):

    def post(self, request, *args, **kwargs):

        location_ids = request.data.get('location_ids', [])
        
        if len(location_ids) < 2:

            return Response({'error': 'Debe haber al menos dos ubicaciones'}, status=status.HTTP_400_BAD_REQUEST)
        
        task = calcular_distancia.apply_async(args=[location_ids])
        
        return Response({'task_id': task.id, 'status': 'Tarea en proceso'}, status=status.HTTP_202_ACCEPTED)

class LocationRegister(APIView):

    def post(self, request, *args, **kwargs):

        serializer = LocationSerializer(data=request.data)

        if serializer.is_valid():

            location = serializer.save()

            return Response({"id": location.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetTaskStatus(APIView):

    def get(self, request, *args, **kwargs):

        task_id = kwargs.get('task_id')
        
        if not task_id:

            return Response({'error': 'Se debe proporcionar un task_id'}, status=status.HTTP_400_BAD_REQUEST)
        
        result = AsyncResult(task_id)
        
        if result.state == 'PENDING':
            status_message = 'Tarea en cola o pendiente'

        elif result.state == 'STARTED':
            status_message = 'Tarea en proceso'

        elif result.state == 'SUCCESS':
            status_message = f'Tarea completada. Resultado: {result.result}'

        elif result.state == 'FAILURE':
            status_message = f'Tarea fallida. Error: {result.result}'

        else:
            status_message = f'Estado desconocido: {result.state}'
            
        
        return Response({'task_id': task_id, 'status': status_message}, status=status.HTTP_200_OK)
