# Generated by Django 4.1.3 on 2022-11-07 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hoteliaApp', '0004_service_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadAdultos', models.IntegerField()),
                ('cantidadNiños', models.IntegerField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoteliaApp.reservation')),
                ('rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoteliaApp.rooms')),
            ],
        ),
    ]