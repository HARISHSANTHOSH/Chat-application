from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import Signupform


# Create your views here.

def frontpage(request):
    return render(request,"frontpage.html")

def signup(request):
    if request.method=='POST':
        form=Signupform(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('frontpage')
    else:
        form=Signupform
    
    return render(request,'signin.html',{"form":form})    


    


