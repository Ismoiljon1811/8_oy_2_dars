from django.shortcuts import render
from django.forms import model_to_dict

from .serializers import *


from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


from .models import Car



class CarAPIView(APIView):
    def get(self,request:Request):
        cars = Car.objects.values()
        return Response({'cars':cars})
    
    def post(self, request:Request):
        cars = Car.objects.create(
           name = request.data['name'],
           color = request.data['color'],
           price = request.data['price'],
           description = request.data['description'] 
        )

        return Response(model_to_dict(cars))
