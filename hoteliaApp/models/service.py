from django.db import models

class Service(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30,null= False)
    costoServicio= models.FloatField(max_length=10, null=False)
    descripcion = models.TextField(max_length= 1000,null=False)