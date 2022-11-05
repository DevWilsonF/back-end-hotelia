from django.db import models
from .account import Account
from .hotel import Hotel

class Reservation(models.Model):
    id = models.AutoField(primary_key= True)
    account = models.ForeignKey(Account,null=False,on_delete=models.PROTECT)
    hotel = models.ForeignKey(Hotel,null=False,on_delete= models.PROTECT)
    fechaReserva = models.DateTimeField(auto_now_add=True, blank=True)
    fechaCheckIn = models.DateField(null=False)
    fechaCheckOut = models.DateField(null=False)
    medioPago= models.CharField(max_length=15,null=False)
    