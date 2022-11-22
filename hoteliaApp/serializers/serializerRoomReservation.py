from rest_framework import serializers
from hoteliaApp.models.roomReservation import RoomReservation

class SerializerRoomReservation(serializers.ModelSerializer):
    class Meta:
        model= RoomReservation
        fields=['id','reservation','rooms','cantidadAdultos','cantidadNiños']
        