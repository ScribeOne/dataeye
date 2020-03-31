from rest_framework import viewsets
from . import models, serializers
from .models import HutEye, HutEyeRecord
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin, UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.response import Response



def index(request):
    return HttpResponse("Hello from dataEye")


"""  
class ModelTypeViewset(viewsets.ModelViewSet):
    queryset = models.ModelType.objects.all()
    serializer_class = serializers.ModelTypeSerializer


class HutViewset(viewsets.ModelViewSet):
    queryset = models.HutEye.objects.all()
    serializer_class = serializers.HutSerializer

class HutRecordView(APIView):
    def get(self, request):
        hut_records = models.HutEyeRecord.objects.all()
        serializer = serializers.HutRecordSerializer(hut_records, many=True)
        print(serializer.data)
        return Response({"records": serializer.data})

    # define handling on POST for HutEyeRecordings
    def post(self, request):
        # check if json contains required fields
        meta_info = request.data.get('channel')
        if not (meta_info):
            return Response({"error": "channel field missing"}, status=400)

        feed = request.data.get('feed')
        if not (feed):
            return Response({"error": "feeds field missing"}, status=400)

        # check if device exists in db
        device_id = meta_info.get('device')
        try:
            huteye = HutEye.objects.get(device_id=device_id)
        except HutEye.DoesNotExist:
            return Response({'error': 'HutEye does not exist'}, status=404)

        # check if fields are valid intergers
        value1 = feed.get('value1')
        if not (isinstance(value1, int)):
            return Response({"error": "'{}' is not valid".format(value1)},
                            status=400)
        value2 = feed.get('value2')
        if not (isinstance(value2, int)):
            return Response({"error": "'{}' is not valid".format(value2)},
                            status=400)

        # save the new record
        huteye_record = HutEyeRecord.objects.create(assosiated_device=huteye,
                                                    field1=value1,
                                                    field2=value2)
                                                    
        return Response({'success': 'record saved'})

 
       serializer = serializers.HutRecordSerializer(data=hut_record)
        if serializer.is_valid(raise_exception=True):
            record_saved = serializer.save() 
        return Response({"success": "Record '{}' created successfully".format(record_saved.device_id)})
"""


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

'''