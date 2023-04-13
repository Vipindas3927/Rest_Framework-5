from rest_framework import serializers
from .models import *

class normalserializer(serializers.Serializer):
    roll = serializers.IntegerField()
    name = serializers.CharField(max_length=20)