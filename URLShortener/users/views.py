from operator import truediv
from django.shortcuts import render
from django.http import HttpResponse
from django. views. decorators. csrf import csrf_exempt
from .models import User

def userAlreadyExists(username,password)->bool:
    existingUsers = User.objects(username=username)
    if len( existingUsers ) >  0:
        return True
    return False

def validateUser(username,password) -> bool:
    
    existingUsers = User.objects(username=username)
    #No existing users or existing user but incorrect password
    if len(existingUsers) ==  0 or existingUsers[0].password != password:
        return False
    return True
        


# Create your views here.
@csrf_exempt
def signupUser(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if userAlreadyExists(username,password):
            return HttpResponse('User already exists')
        user = User(username = username,password = password)
        user.save()
        return HttpResponse(username)
    return HttpResponse("GET Request -> A form will be rendered to sign up user")

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not validateUser(username,password):
            return HttpResponse('Username or password incorrect')
        return HttpResponse(username)  
    return HttpResponse('GET Request -> A form will be rendered to login user')

