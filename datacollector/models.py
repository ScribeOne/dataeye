from django.db import models

# define different types of availaible sensors
SENSOR_TYPE_CHOICES = [('TEMP', 'Temperature'), ('HUMI', 'Humidity'),
                       ('DUST', 'Fine dust'), ('WIND', 'Wind speed')]


class ModelType(models.Model):
    model_name = models.CharField(max_length=255, unique=True)
    model_id = models.CharField(max_length=50, unique=True)
    dev_start = models.DateField(default=None, null=True, blank=True)
    release_date = models.DateField(default=None, null=True, blank=True)


class Device(models.Model):
    device_id = models.CharField(max_length=16)
    device_name = models.CharField(max_length=255)
    model_type = models.ForeignKey(ModelType, on_delete=models.PROTECT)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    active = models.BooleanField(default=True)
    public = models.BooleanField(default=False)
    manufactured = models.DateField(default=None, null=True, blank=True)

    class Meta:
        abstract = True


class DustEye(Device):
    field1 = models.CharField(max_length=4,
                              choices=SENSOR_TYPE_CHOICES,
                              default='TEMP')
    field2 = models.CharField(max_length=4,
                              choices=SENSOR_TYPE_CHOICES,
                              default='HUMI')
    field3 = models.CharField(max_length=4,
                              choices=SENSOR_TYPE_CHOICES,
                              default='DUST')
    field4 = models.CharField(max_length=4,
                              choices=SENSOR_TYPE_CHOICES,
                              default='WIND')


class DustEyeRecord(models.Model):
    pass


class HutEye(Device):
    field1 = models.CharField(max_length=4,
                              choices=SENSOR_TYPE_CHOICES,
                              default='TEMP')
    field2 = models.CharField(max_length=4,
                              choices=SENSOR_TYPE_CHOICES,
                              default='HUMI')


class HutEyeRecord(models.Model):
    assosiated_device = models.ForeignKey(HutEye, on_delete=models.CASCADE)
    field1 = models.FloatField(blank=True, null=True, default=0.0)
    field2 = models.FloatField(blank=True, null=True, default=0.0)