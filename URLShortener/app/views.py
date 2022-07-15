from django.shortcuts import render
from django.http import HttpResponse
from django. views. decorators. csrf import csrf_exempt
from app.models import User,ShortURL


def generateRandomShortUrl(url) -> str:
    #code to genrate random short url form given url
    return "abc"

# Create your views here.

def landing(request):
    return HttpResponse("You can either login here or sign up")

@csrf_exempt
def signupUser(request) :
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        existingUsers = User.objects(username=username)
        if len( existingUsers ) >  0:
            return HttpResponse('User already exists')
        user = User(username = username,password = password)
        user.save()
        return HttpResponse("User has been added to DB")
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


#this view must be protected -> only nlogged in user should be able to access this view
@csrf_exempt
def homeView(request):

    if request.method == 'POST':
        originalURL = request.POST.get('originalURL')

        existingShortURL = ShortURL.objects(originalURL = originalURL)

        #problem if different users try to shorten same URL -> possibly authentication will take care of it ??
        if len(existingShortURL) > 0:
            return HttpResponse('For specified URL , a shortened URL has already been created')

        methodOfGeneration = request.POST.get('methodOfGeneration')
        modifiedURL = "short.ly/"
        if methodOfGeneration == 'manual':
            modifiedURL += request.POST.get('manualShortURL')
        elif methodOfGeneration == 'auto':
            modifiedURL += generateRandomShortUrl(originalURL)

        shortURL = ShortURL(shortURL = modifiedURL,originalURL = originalURL,hitCount = 0)
        shortURL.save()

        return HttpResponse(originalURL  + "  " + modifiedURL + "  "+ methodOfGeneration)

    return HttpResponse("GET Request -> A form , to enter the URL to be shortened , is rendered")
