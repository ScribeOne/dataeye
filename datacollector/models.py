from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# define different types of availaible sensors
SENSOR_TYPE_CHOICES = [('TEMP', 'Temperature'), ('HUMI', 'Humidity'),
                       ('DUST', 'Fine dust'), ('WIND', 'Wind speed')]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adress = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.object.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.Profile.save()


class ModelType(models.Model):
    model_name = models.CharField(max_length=255, unique=True)
    model_id = models.CharField(max_length=50, unique=True)
    dev_start = models.DateField(default=None, null=True, blank=True)
    release_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return self.model_id


class Device(models.Model):
    owner = models.ForeignKey(User,
                              on_delete=models.PROTECT,
                              null=True,
                              blank=True)
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

    def __str__(self):
        return self.device_id


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

    def __str__(self):
        return "test"