from operator import truediv
from urllib.request import Request
from django.shortcuts import render
from django.http import HttpResponse
from django. views. decorators. csrf import csrf_exempt
from .models import ShortURL
from users.models import User


def generateRandomShortUrl(url : str) -> str:
    #code to genrate random short url form given url
    return "abc"

def authenticateUser(request : Request) -> User:
    if not "username" in request.headers.keys():    
        return None
    username = request.headers['username']
    user = User.objects(username = username )[0]
    return user

def URLAlreadyShortenedByUser(user : User , originalURL : str ) -> bool :
    shortURLsForOriginalURL = ShortURL.objects(originalURL = originalURL)
    for shortURL in shortURLsForOriginalURL:
        # print(type(shortURL.user) , shortURL.user , '='*20)
        if shortURL.user == user:
            return True
    return False

def getShortenedURL( originalURL : str , methodOfGeneration : str , request : Request )-> str:
    if methodOfGeneration == 'manual':
            return request.POST.get('manualShortURL')
    return generateRandomShortUrl(originalURL)


# Create your views here.

def landing(request):
    return HttpResponse("You can either login here or sign up")


#this view must be protected -> only logged in user should be able to access this view
@csrf_exempt
def homeView(request):

    # print(request.headers , "==="*30)
    # print(request.META.keys() , "==="*30)
    user = authenticateUser(request)


    if user == None:
        return HttpResponse('Not authenticated to access this URL')

    if request.method == 'POST':
        originalURL = request.POST.get('originalURL')

        if URLAlreadyShortenedByUser(user,originalURL):
            return HttpResponse('For specified URL , a shortened URL has already been created by user')

        methodOfGeneration = request.POST.get('methodOfGeneration')
        modifiedURL = "http://127.0.0.1:8000/"

        modifiedURL += getShortenedURL(originalURL,methodOfGeneration,request)

        shortURL = ShortURL(shortURL = modifiedURL,originalURL = originalURL,hitCount = 0,user = user)
        shortURL.save()

        return HttpResponse('Your URL has been shortened')

    return HttpResponse("GET Request -> A form , to enter the URL to be shortened , is rendered")
