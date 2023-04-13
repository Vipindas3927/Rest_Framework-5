from django.db import models

# Create your models here.
class sample(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=20)
