from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing), #display login and signup options 
    path('home',views.homeView), #display home page where url to be shortened is entered (this url should be protected)
]