from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=255)
    devtime = models.DateTimeField(auto_now_add=True)
    golive = models.DateTimeField(auto_now_add=True)

class Measurement(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    value01 = models.IntegerField()
    value02 = models.IntegerField()
    timestamp = models.CharField(max_length=55, default="no timestamp")

class Model(models.Model):
    name = models.CharField(max_length=255)
