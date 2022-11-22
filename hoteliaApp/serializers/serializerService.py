from hoteliaApp.models.service import Service
from rest_framework import serializers

class SerializerService (serializers.ModelSerializer):
    class Meta:
        model= Service
        fields = ['id','nombre','costoServicio','descripcion']