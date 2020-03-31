from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import HutRecordSerializer
from datacollector.models import HutEye, HutEyeRecord

class HutRecordView(APIView):
    def get(self, request):
        hut_records = HutEyeRecord.objects.all()
        serializer = HutRecordSerializer(hut_records, many=True)
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