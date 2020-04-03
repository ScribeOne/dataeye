# Generated by Django 3.0.4 on 2020-04-01 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DustEyeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HutEye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=16)),
                ('device_name', models.CharField(max_length=255)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('public', models.BooleanField(default=False)),
                ('manufactured', models.DateField(blank=True, default=None, null=True)),
                ('field1', models.CharField(choices=[('TEMP', 'Temperature'), ('HUMI', 'Humidity'), ('DUST', 'Fine dust'), ('WIND', 'Wind speed')], default='TEMP', max_length=4)),
                ('field2', models.CharField(choices=[('TEMP', 'Temperature'), ('HUMI', 'Humidity'), ('DUST', 'Fine dust'), ('WIND', 'Wind speed')], default='HUMI', max_length=4)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ModelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=255, unique=True)),
                ('model_id', models.CharField(max_length=50, unique=True)),
                ('dev_start', models.DateField(blank=True, default=None, null=True)),
                ('release_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HutEyeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.FloatField(blank=True, default=0.0, null=True)),
                ('field2', models.FloatField(blank=True, default=0.0, null=True)),
                ('assosiated_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datacollector.HutEye')),
            ],
        ),
        migrations.AddField(
            model_name='huteye',
            name='model_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='datacollector.ModelType'),
        ),
        migrations.CreateModel(
            name='DustEye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=16)),
                ('device_name', models.CharField(max_length=255)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('public', models.BooleanField(default=False)),
                ('manufactured', models.DateField(blank=True, default=None, null=True)),
                ('field1', models.CharField(choices=[('TEMP', 'Temperature'), ('HUMI', 'Humidity'), ('DUST', 'Fine dust'), ('WIND', 'Wind speed')], default='TEMP', max_length=4)),
                ('field2', models.CharField(choices=[('TEMP', 'Temperature'), ('HUMI', 'Humidity'), ('DUST', 'Fine dust'), ('WIND', 'Wind speed')], default='HUMI', max_length=4)),
                ('field3', models.CharField(choices=[('TEMP', 'Temperature'), ('HUMI', 'Humidity'), ('DUST', 'Fine dust'), ('WIND', 'Wind speed')], default='DUST', max_length=4)),
                ('field4', models.CharField(choices=[('TEMP', 'Temperature'), ('HUMI', 'Humidity'), ('DUST', 'Fine dust'), ('WIND', 'Wind speed')], default='WIND', max_length=4)),
                ('model_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='datacollector.ModelType')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
