from rest_framework import serializers
from rest_framework.decorators import api_view
from . import models


class ModelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelType
        fields = '__all__'


class HutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HutEye
        fields = '__all__'