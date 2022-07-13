from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return HttpResponse("You can either login here or sign up")