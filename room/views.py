from django.shortcuts import render
from .models import Room,Message
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
@login_required
def rooms(request):
    rooms=Room.objects.all()
    return render(request,"rooms.html",{"rooms":rooms})

@login_required
def room(request,slug):
    room=Room.objects.get(slug=slug)
    messages=Message.objects.filter(room=room)
    return render(request,'room.html',{"room":room,"messages":messages})

    

