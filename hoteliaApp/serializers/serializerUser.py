from rest_framework import serializers
from hoteliaApp.models.users import User
from hoteliaApp.models.account import Account
from hoteliaApp.serializers.serializerAccount import SerializerAccount


class SerializerUser(serializers.ModelSerializer):
    account = SerializerAccount()
    class Meta:
        model = User
        fields = ['id','username','password','Estado','account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        print(userInstance)
        return userInstance 
    def update(self,instance,validatad_data):
        instance.username = validatad_data.get('username',instance.username)
        instance.password = validatad_data.get('password',instance.password)
        instance.Estado= validatad_data.get('Estado',instance.Estado)
        instance.save()
        return instance
     
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user = obj.id)
        return {
            "id": user.id,
            "username" : user.username,
            "Estado": user.Estado,
            "account" :{
                "id": account.id,
                "Nombre": account.Nombre,
                "Apellido": account.Apellido,
                "Telefono": account.Telefono,
                "Genero": account.Genero,
                "TipoDocumento": account.TipoDocumento,
                "NumeroDocumento": account.NumeroDocumento,
                "Direccion": account.Direccion,
                "Ciudad": account.Ciudad,
                "FechaNacimiento": account.FechaNacimiento,
                "Correo": account.Correo,
                "Rol": account.Rol
            }
        }