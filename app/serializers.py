from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

import io

from .models import Car



class CarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    color = serializers.CharField(max_length = 80)
    price = serializers.IntegerField()
    description = serializers.CharField()



    def serialization():
        object_example = Car.objects.all().first()
        print(object_example)
        serializer = CarSerializer(object_example)
        print(serializer)
        json = JSONRenderer().render(serializer.data)
        print(json)

    def daserialisation():
        json = b'{"name":"Cobalt","color":"white","price":12000,"description":"This is Cobalt. Chevrolet Cobalt is a car developed by General Motors. This car is produced in four variants."}'
        stream = io.BytesIO(json)
        data = JSONParser().parse(stream)
        serializer = CarSerializer(data=data)
        serializer.is_valid()
        print(serializer.validated_data)
