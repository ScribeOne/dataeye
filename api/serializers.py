from rest_framework import serializers
from datacollector.models import HutEyeRecord, HutEye, ModelType

class HutSerializer(serializers.ModelSerializer):
    class Meta:
        model = HutEye
        fields = '__all__'


class HutRecordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = HutEyeRecord
        fields = '__all__'
        depth = 1


class ModelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelType
        fields = '__all__'

