from hoteliaApp.models.account import Account
from rest_framework import serializers

class SerializerAccount(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['Nombre','Apellido','Telefono','Genero','TipoDocumento','NumeroDocumento','Direccion','Ciudad','FechaNacimiento','Correo','Rol']

