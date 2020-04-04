from rest_framework import serializers
from datacollector.models import HutEyeRecord, HutEye, ModelType, Profile
from django.contrib.auth.models import User


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


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = '__all__'
        depth = 1