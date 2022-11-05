from django.db import models
from .users import User
   
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='account', on_delete=models.CASCADE)
    Nombre=models.CharField('Nombre', max_length=30,null=False)
    Apellido=models.CharField('Apellido',max_length=30,null=False)
    Telefono=models.CharField('Telefono', max_length=30,null=False)
    Genero=models.CharField('Genero', max_length=30,null=False)
    TipoDocumento=models.CharField('TipoDocumento', max_length=30,null=False)
    NumeroDocumento=models.CharField('NumeroDocumento', max_length=30,null=False)
    Direccion=models.CharField('Direccion', max_length=120,null=False)
    Ciudad=models.CharField('Ciudad', max_length=30,null=False)
    FechaNacimiento=models.DateField('FechaNacimiento',null=False)
    Correo=models.EmailField('Correo', max_length=30,null=False)
    Rol=models.CharField('Rol', max_length=30,null=False)