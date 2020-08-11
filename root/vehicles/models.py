from django.conf import settings
from django.db import models


class Vehicle(models.Model):
    plate = models.CharField(max_length=255, unique=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='vehicles', on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
