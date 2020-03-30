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


class HutRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HutEyeRecord
        fields = ('assosiated_device', 'field1', 'field2')

    


