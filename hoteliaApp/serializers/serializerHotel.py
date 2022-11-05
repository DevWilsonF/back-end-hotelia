from rest_framework import serializers
from hoteliaApp.models.hotel import Hotel


class SerializerHotel(serializers.ModelSerializer):
    class Meta:
        model= Hotel
        fields=['id','user','nombre_hotel','telefono_hotel','direccion_hotel','ciudad_hotel','pais_hotel','descripcion_hotel','estado_hotel']

        
