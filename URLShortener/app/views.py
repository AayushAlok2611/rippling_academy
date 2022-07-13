from django.shortcuts import render
from django.http import HttpResponse
from app.models import UserModel
from django. views. decorators. csrf import csrf_exempt

# Create your views here.

#landing page -> first tthing visible to an unauthenticated user
def landing(request):
    return HttpResponse("You can either login here or sign up")


#testing if adding to db works

