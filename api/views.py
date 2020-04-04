from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, AllowAny
from rest_framework import authentication

from .serializers import HutRecordSerializer, HutSerializer, UserSerializer
from datacollector.models import HutEye, HutEyeRecord, ModelType


class HutRecordView(APIView):
    def get(self, request):
        hut_records = HutEyeRecord.objects.all()
        serializer = HutRecordSerializer(hut_records, many=True)
        return Response(serializer.data)

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
        if not device_id:
            return Response({"error": "device field missing"}, status=400)
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

        return Response({'success': 'record saved'}, status=201)


@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['GET'])
def devicerecord(request, id):
    records = HutEyeRecord.objects.filter(assosiated_device=id)
    serializer = HutRecordSerializer(records, many=True)
    return Response(serializer.data)


@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def userdevice(request):
    hut_eyes = HutEye.objects.filter(owner=request.user)
    serializer = HutSerializer(hut_eyes, many=True)
    return Response(serializer.data)


@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def report(request):
    return Response({"message": "Hello from request", "data": request.data})


@authentication_classes([authentication.TokenAuthentication])
@permission_classes([IsAuthenticated])
class Dev(APIView):
    def get(self, request):
        content = {'message': 'Hello'}
        return Response(content)
