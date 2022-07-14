from django.shortcuts import render
from django.http import HttpResponse
from django. views. decorators. csrf import csrf_exempt
from app.models import User,ShortURL

# Create your views here.

def landing(request):
    return HttpResponse("You can either login here or sign up")

@csrf_exempt
def signupUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        existingUsers = User.objects(username=username)
        if len( existingUsers ) >  0:
            return HttpResponse('User already exists')
        user = User(username = username,password = password)
        user.save()
        print(user.id)
        s = str(username) + "  " + str(password)
        return HttpResponse(s)
    return HttpResponse("GET Request -> A form will be rendered to sign up user")

@csrf_exempt
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        existingUsers = User.objects(username=username)

        #No existing users or existing user but incorrect password
        if len(existingUsers) ==  0 or existingUsers[0].password != password:
            return HttpResponse('Username or password incorrect')
        return HttpResponse('You are logged in')
        
    return HttpResponse('GET Request -> A form will be rendered to login user')
