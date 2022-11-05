from django.db import models
from .hotel import Hotel

class Rooms(models.Model):
    id= models.AutoField(primary_key=True)
    hotel= models.ForeignKey(Hotel,on_delete=models.CASCADE,null=False)
    nombre = models.CharField(max_length=30,null=False)
    estado = models.BooleanField(null=False,default=True)
    descripcion= models.TextField(max_length=1000,null=False)
    costoNoche= models.FloatField(max_length=9, null = False )
    