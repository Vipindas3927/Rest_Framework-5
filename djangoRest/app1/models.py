from django.db import models
from rest_framework import serializers


# Create your models here.
class sample(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=20)

