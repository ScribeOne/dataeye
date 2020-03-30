from rest_framework import viewsets
from . import models, serializers
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView


class ModelTypeViewset(viewsets.ModelViewSet):
    queryset = models.ModelType.objects.all()
    serializer_class = serializers.ModelTypeSerializer


class HutViewset(viewsets.ModelViewSet):
    queryset = models.HutEye.objects.all()
    serializer_class = serializers.HutSerializer


'''
class HutRecordViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HutRecordSerializer
    queryset = models.HutEyeRecord.objects.all()

    def post(self, request, pk, format=None):
        serializer = serializers.HutRecordSerializer(data=request.data)
        print(serializer)
        return HttpResponse(content='Test')
    
    def get_queryset(self):
        return super().get_queryset()



class HutRecordViewSet(
        GenericViewSet,  # generic stuff
        CreateModelMixin,  # POST
        RetrieveModelMixin,  # GET for one
        UpdateModelMixin,  # PUT/PATCH
        ListModelMixin):  # GET for many

    serializer_class = serializers.HutRecordSerializer
    queryset = models.HutEyeRecord.objects.all()


def post(self, request):
    print(request.data)

def get(self, request):
    return "test"
'''

class HutRecordViewSet(
        GenericViewSet,  # generic stuff
        CreateModelMixin,  # POST
        RetrieveModelMixin,  # GET for one
        UpdateModelMixin,  # PUT/PATCH
        ListModelMixin):  # GET for many

    serializer_class = serializers.HutRecordSerializer
    queryset = models.HutEyeRecord.objects.all()

    def post(self, request):
        print(request.data)
        return HttpResponse(content="test123")

    def get(self, request):
        print(request.data)
        return HttpResponse(content="test123")
