from rest_framework.response import Response
from rest_framework.decorators import api_view
from hoteliaApp.models.account import Account
from hoteliaApp.serializers.serializerAccount import SerializerAccount

@api_view(['GET','PUT','DELETE'])
def account_unique_view(request,pk=None):
    account = Account.objects.filter(user=pk).first()
    if request.method == 'GET':
        account_serializer = SerializerAccount(account)
        return Response(account_serializer.data)

    elif request.method == 'PUT':
        request.data
        account_serializers = SerializerAccount(account,data=request.data)
        if  account_serializers.is_valid():
            account_serializers.save()
            return Response(account_serializers.data)
        return Response(account_serializers.errors)
    
    elif request.method == 'DELETE':
        account.delete()
        return Response('Eliminado')