"""hoteliaProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#estas son las url que se van a consumir mediante peticiones rest
from django.contrib import admin
from django.urls import path
from hoteliaApp import views
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('user/',views.UserPostView.as_view()),
    path('user/<int:pk>',views.UserGetView.as_view()),
    path('account/<int:pk>',views.account_unique_view),
    path('hotel/',views.hotelAllView),
    path('hotel/<int:pk>',views.hotelUniqueView),
    path('hotel/user/<int:pk>',views.hotelUniqueUserView),
    path('rooms/',views.roomAllView),
    path('room/hotel/<int:pk>',views.roomUniqueUserView),
    path('room/<int:pk>',views.roomUniqueView),
    path('service/',views.serviceAllView),
    path('service/<int:pk>',views.serviceUniqueView),
    path('reservation/',views.reservationAllView),
    path('reservation/<int:pk>',views.reservationUniqueView),
    path('reservation/user/<int:pk>',views.reservationUniqueUserView),
    path('reservation/hotel/<int:pk>',views.reservationUniqueHotelView),
    path('roomreservartion/',views.roomReservationAllView),
    path('roomreservation/<int:pk>',views.roomReservationUniqueView),
    path('roomreservation/reservation/<int:pk>',views.roomReservationUniqueReservationView),
    path('roomreservation/room/<int:pk>',views.roomReservationUniqueRoomView),
]
