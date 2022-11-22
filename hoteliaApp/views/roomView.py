from rest_framework.response import Response
from rest_framework.decorators import api_view
from hoteliaApp.models.rooms import Rooms
from hoteliaApp.serializers.serializerRoom import SerializerRoom

@api_view(['GET','POST'])
def roomAllView(request):
    if request.method =='GET':
        room = Rooms.objects.all()
        room_serializer = SerializerRoom(room,many=True)
        return Response (room_serializer.data)
    
    elif request.method =='POST':
        rom_serializer = SerializerRoom(data=request.data)
        if  rom_serializer.is_valid():
            rom_serializer.save()
            return Response(rom_serializer.data)
        return Response(rom_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def roomUniqueUserView(request,pk=None):
    room = Rooms.objects.filter(hotel = pk)
    if request.method == 'GET':
        
        room_serializer = SerializerRoom(room,many=True)
        return Response(room_serializer.data)
    
@api_view(['GET','PUT','DELETE'])
def roomUniqueView(request,pk=None):
    room = Rooms.objects.filter(id = pk).first()
    if request.method == 'GET':
        room_serializer = SerializerRoom(room)
        return Response(room_serializer.data)

    elif request.method == 'PUT':
        
        request.data
        room_serializers = SerializerRoom(room,data=request.data)
        if  room_serializers.is_valid():
            room_serializers.save()
            return Response(room_serializers.data)
        return Response(room_serializers.errors)
    
    elif request.method == 'DELETE':
        room.delete()
        return Response('Eliminado')