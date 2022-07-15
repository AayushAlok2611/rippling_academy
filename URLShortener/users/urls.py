from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup',views.signupUser), #display signup page
    path('login',views.loginUser),  #display login page
]