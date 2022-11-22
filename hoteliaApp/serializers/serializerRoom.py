from rest_framework import serializers
from hoteliaApp.models.rooms import Rooms

class SerializerRoom(serializers.ModelSerializer):
    
    class Meta:
        model = Rooms
        fields=['id','hotel','nombre','estado','descripcion','costoNoche']