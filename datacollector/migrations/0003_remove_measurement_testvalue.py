# Generated by Django 3.0.4 on 2020-03-27 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datacollector', '0002_measurement_testvalue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='measurement',
            name='testvalue',
        ),
    ]