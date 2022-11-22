from rest_framework import serializers
from hoteliaApp.models.reservation import Reservation

class SerializerReservation(serializers.ModelSerializer):
    class Meta:
        model= Reservation
        fields= ['id','account','hotel','fechaReserva','fechaCheckIn','fechaCheckOut','medioPago']