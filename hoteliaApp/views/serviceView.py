from rest_framework.response import Response
from rest_framework.decorators import api_view
from hoteliaApp.models.service import Service
from hoteliaApp.serializers.serializerService import SerializerService
# esta es la parte  visual del componente la cual va a enviar las peticiones rest
@api_view(['GET','POST'])
def serviceAllView(request):
    if request.method =='GET':
        service = Service.objects.all()
        service_serializer = SerializerService(service,many=True)
        return Response (service_serializer.data)
    
    elif request.method =='POST':
        serv_serializer = SerializerService(data=request.data)
        if  serv_serializer.is_valid():
            serv_serializer.save()
            return Response(serv_serializer.data)
        return Response(serv_serializer.errors)

    
@api_view(['GET','PUT','DELETE'])
def serviceUniqueView(request,pk=None):
    service = Service.objects.filter(id = pk).first()
    if request.method == 'GET':
        service_serializer = SerializerService(service)
        return Response(service_serializer.data)

    elif request.method == 'PUT':
        
        request.data
        service_serializers = SerializerService(service,data=request.data)
        if  service_serializers.is_valid():
            service_serializers.save()
            return Response(service_serializers.data)
        return Response(service_serializers.errors)
    
    elif request.method == 'DELETE':
        service.delete()
        return Response('Eliminado')