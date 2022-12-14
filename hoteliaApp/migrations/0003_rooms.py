# Generated by Django 4.1.3 on 2022-11-04 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoteliaApp', '0002_hotel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('estado', models.BooleanField(default=True)),
                ('descripcion', models.TextField(max_length=1000)),
                ('costoNoche', models.FloatField(max_length=9)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoteliaApp.hotel')),
            ],
        ),
    ]
