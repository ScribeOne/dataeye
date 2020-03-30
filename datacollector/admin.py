from django.contrib import admin
from .models import HutEye, ModelType, HutEyeRecord

admin.site.register(ModelType)
admin.site.register(HutEye)
admin.site.register(HutEyeRecord)
