from django.urls import path
from .import views
from django.urls import reverse
from .views import *

# Assuming you have a view named 'room_detail' that takes a 'slug' parameter
# and 'room' is an instance of your Room model with a 'slug' attribute




urlpatterns=[
    path('',views.rooms,name='rooms'),
    path('(?<slug:slug>/', views.room, name='room'),
]
   
   






