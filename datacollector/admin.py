from django.contrib import admin
from .models import HutEye, ModelType, HutEyeRecord, Profile

admin.site.register(ModelType)
admin.site.register(HutEye)
admin.site.register(HutEyeRecord)
admin.site.register(Profile)
