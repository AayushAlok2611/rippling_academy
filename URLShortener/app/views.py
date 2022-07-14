from django.shortcuts import render
from django.http import HttpResponse
from django. views. decorators. csrf import csrf_exempt
from app.models import User,ShortURL

# Create your views here.

#landing page -> first tthing visible to an unauthenticated user
def landing(request):
    return HttpResponse("You can either login here or sign up")


#testing if adding to db works
@csrf_exempt
def signupUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        if len(User.objects(username=username)) !=  0:
            return HttpResponse('User already exists')
        user = User(username = username,password = password)
        user.save()
        s = str(username) + "  " + str(password)
        return HttpResponse(s)
    return HttpResponse("GET Request -> A form will be rendered to sign up user")
