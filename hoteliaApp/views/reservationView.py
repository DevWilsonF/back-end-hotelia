from rest_framework.response import Response
from rest_framework.decorators import api_view
from hoteliaApp.models.reservation import Reservation
from hoteliaApp.serializers.serializerReservation import SerializerReservation

@api_view(['GET','POST'])
def reservationAllView(request):
    if request.method =='GET':
        reservation = Reservation.objects.all()
        reservation_serializer = SerializerReservation(reservation,many=True)
        return Response (reservation_serializer.data)
    
    elif request.method =='POST':
        res_serializer = SerializerReservation(data=request.data)
        if  res_serializer.is_valid():
            res_serializer.save()
            return Response(res_serializer.data)
        return Response(res_serializer.errors)

@api_view(['GET'])
def reservationUniqueUserView(request,pk=None):
    reservation = Reservation.objects.filter(account = pk)
    if request.method == 'GET':
        
        reservation_serializer = SerializerReservation(reservation,many=True)
        return Response(reservation_serializer.data)
@api_view(['GET'])
def reservationUniqueHotelView(request,pk=None):
    reservation = Reservation.objects.filter(hotel = pk)
    if request.method == 'GET':
        
        reservation_serializer = SerializerReservation(reservation,many=True)
        return Response(reservation_serializer.data)
    
@api_view(['GET','PUT','DELETE'])
def reservationUniqueView(request,pk=None):
    reservation = Reservation.objects.filter(account = pk).first()
    if request.method == 'GET':
        
        reservation_serializer = SerializerReservation(reservation)
        return Response(reservation_serializer.data)

    elif request.method == 'PUT':
        request.data
        reservation_serializers = SerializerReservation(reservation,data=request.data)
        if  reservation_serializers.is_valid():
            reservation_serializers.save()
            return Response(reservation_serializers.data)
        return Response(reservation_serializers.errors)
    
    elif request.method == 'DELETE':
        reservation.delete()
        return Response('Eliminado')