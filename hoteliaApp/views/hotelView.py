from rest_framework.response import Response
from rest_framework.decorators import api_view
from hoteliaApp.models.hotel import Hotel
from hoteliaApp.serializers.serializerHotel import SerializerHotel

@api_view(['GET','POST'])
def hotelAllView(request):
    if request.method =='GET':
        hotel = Hotel.objects.all()
        hotel_serializer = SerializerHotel(hotel,many=True)
        return Response (hotel_serializer.data)
    
    elif request.method =='POST':
        per_serializer = SerializerHotel(data=request.data)
        if  per_serializer.is_valid():
            per_serializer.save()
            return Response(per_serializer.data)
        return Response(per_serializer.errors)

@api_view(['GET','PUT','DELETE'])
def hotelUniqueUserView(request,pk=None):
    hotel = Hotel.objects.filter(user = pk)
    if request.method == 'GET':
        
        hotel_serializer = SerializerHotel(hotel,many=True)
        return Response(hotel_serializer.data)
    
@api_view(['GET','PUT','DELETE'])
def hotelUniqueView(request,pk=None):
    hotel = Hotel.objects.filter(id = pk).first()
    if request.method == 'GET':
        hotel_serializer = SerializerHotel(hotel)
        return Response(hotel_serializer.data)

    elif request.method == 'PUT':
        
        request.data
        hotel_serializers = SerializerHotel(hotel,data=request.data)
        if  hotel_serializers.is_valid():
            hotel_serializers.save()
            return Response(hotel_serializers.data)
        return Response(hotel_serializers.errors)
    
    elif request.method == 'DELETE':
        hotel.delete()
        return Response('Eliminado')
    