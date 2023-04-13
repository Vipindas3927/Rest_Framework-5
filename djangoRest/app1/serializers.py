from rest_framework import serializers
from .models import *


class normalserializer(serializers.Serializer):
    roll = serializers.IntegerField
    name = serializers.CharField(max_length=20)


class modelserializer(serializers.ModelSerializer):
    class Meta:
        model = sample
        fields = '__all__'
