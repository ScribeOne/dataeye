from rest_framework import serializers
from . import models


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Model
        fields = '__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Device
        fields = '__all__'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Measurement
        fields = '__all__'
