from django.urls import path
from .views import *
from core import views 
from django.contrib.auth import views as auth_views

urlpatterns=[


    path('frontpage/', views.frontpage, name='frontpage'),
    path('signup/',views.signup,name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html')),
   
    path("logout/",auth_views.LogoutView.as_view(),name='logout')
   
    
]