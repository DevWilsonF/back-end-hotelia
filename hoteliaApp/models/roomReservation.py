from django.db import models
from .reservation import Reservation
from .rooms import Rooms

class RoomReservation(models.Model):
    id= models.AutoField(primary_key=True)
    reservation = models.ForeignKey(Reservation, null=False,on_delete=models.CASCADE)
    rooms = models.ForeignKey(Rooms,null=False,on_delete=models.CASCADE)
    cantidadAdultos = models.IntegerField(null=False)
    cantidadNiños = models.IntegerField(null=False)