from rest_framework import viewsets
from . import models, serializers
from django.shortcuts import render
from django.http import HttpResponse

class ModelViewset(viewsets.ModelViewSet):
    queryset = models.Model.objects.all()
    serializer_class = serializers.ModelSerializer

class DeviceViewset(viewsets.ModelViewSet):
    queryset = models.Device.objects.all()
    serializer_class = serializers.DeviceSerializer


class MeasurementViewset(viewsets.ModelViewSet):
    queryset = models.Measurement.objects.all()
    serializer_class = serializers.MeasurementSerializer


def index(request):
    return HttpResponse("Hello World from datacollector!")
