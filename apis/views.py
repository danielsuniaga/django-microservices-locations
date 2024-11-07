# Django imports
from django.shortcuts import render
from django.db import connection

# Rest Framework imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class LocationRegister(APIView):

    data = None

    def __init__(self):

        self.data = case_data.cases_data()

    def post(self, request, format=None):

        return Response(True)
