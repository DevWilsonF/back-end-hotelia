from django.contrib import admin
from .models.users import User
from .models.account import Account
from .models.hotel import Hotel
from .models.rooms import Rooms
from .models.reservation import Reservation
from .models.service import Service
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Hotel)
admin.site.register(Rooms)
admin.site.register(Reservation)
admin.site.register(Service)

