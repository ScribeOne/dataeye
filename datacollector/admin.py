from django.contrib import admin
from .models import Device, Measurement, Model

admin.site.register(Model)
admin.site.register(Device)
admin.site.register(Measurement)
