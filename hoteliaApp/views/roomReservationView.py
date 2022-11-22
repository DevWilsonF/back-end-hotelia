from rest_framework.response import Response
from rest_framework.decorators import api_view
from hoteliaApp.models.roomReservation import RoomReservation
from hoteliaApp.serializers.serializerRoomReservation import SerializerRoomReservation


@api_view(['GET','POST'])
def roomReservationAllView(request):
    if request.method =='GET':
        roomReservation = RoomReservation.objects.all()
        roomReservation_serializer = SerializerRoomReservation(roomReservation,many=True)
        return Response (roomReservation_serializer.data)
    
    elif request.method =='POST':
        rResevation_serializer = SerializerRoomReservation(data=request.data)
        if  rResevation_serializer.is_valid():
            rResevation_serializer.save()
            return Response(rResevation_serializer.data)
        return Response(rResevation_serializer.errors)

@api_view(['GET'])
def roomReservationUniqueReservationView(request,pk=None):
    roomReservation = RoomReservation.objects.filter(reservation = pk)
    if request.method == 'GET':
        
        roomReservation_serializer = SerializerRoomReservation(roomReservation,many=True)
        return Response(roomReservation_serializer.data)

@api_view(['GET'])
def roomReservationUniqueRoomView(request,pk=None):
    roomReservation = RoomReservation.objects.filter(room = pk)
    if request.method == 'GET':
        
        roomReservation_serializer = SerializerRoomReservation(roomReservation,many=True)
        return Response(roomReservation_serializer.data)
 
    
@api_view(['GET','PUT','DELETE'])
def roomReservationUniqueView(request,pk=None):
    roomReservation = RoomReservation.objects.filter(id = pk).first()
    if request.method == 'GET':
        roomReservation_serializer = SerializerRoomReservation(roomReservation)
        return Response(roomReservation_serializer.data)

    elif request.method == 'PUT':
        
        request.data
        roomReservation_serializers = SerializerRoomReservation(roomReservation,data=request.data)
        if  roomReservation_serializers.is_valid():
            roomReservation_serializers.save()
            return Response(roomReservation_serializers.data)
        return Response(roomReservation_serializers.errors)
    
    elif request.method == 'DELETE':
        roomReservation.delete()
        return Response('Eliminado')