from django.db import models
from .account import Account
class Hotel(models.Model):
    id= models.AutoField(primary_key=True)
    user= models.ForeignKey(Account, on_delete=models.CASCADE)
    nombre_hotel= models.CharField('Nombre',max_length=30,null=False)
    telefono_hotel= models.CharField('Telefono',max_length=15,null=False)
    direccion_hotel=models.CharField('Direccion', max_length=120,null=False)
    ciudad_hotel=models.CharField('Ciudad', max_length=30,null=False)
    pais_hotel=models.CharField('Pais',max_length=30, null=False)
    descripcion_hotel=models.TextField('Descripcion', max_length=1000,null=False)
    estado_hotel=models.BooleanField('Estado',null=False,default=True)