from rest_framework import serializers
from datacollector.models import HutEyeRecord

class HutRecordSerializer(serializers.Serializer):
    assosiated_device_id = serializers.IntegerField()
    field1 = serializers.FloatField()
    field2 = serializers.FloatField()

    def create(self, validated_data):
        return HutEyeRecord.objects.create(**validated_data)