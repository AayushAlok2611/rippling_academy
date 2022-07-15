from django.shortcuts import render
from django.http import HttpResponse
from django. views. decorators. csrf import csrf_exempt
from .models import ShortURL


def generateRandomShortUrl(url) -> str:
    #code to genrate random short url form given url
    return "abc"

def authenticateUser(request)-> str:
    if "username" in request.META.keys():    
        username = request.META['username']
        return username
    return ""


# Create your views here.

def landing(request):
    return HttpResponse("You can either login here or sign up")


#this view must be protected -> only logged in user should be able to access this view
@csrf_exempt
def homeView(request):

    user = authenticateUser(request)

    if len(user)==0:
        return HttpResponse('Not authenticated to access this URL')

    if request.method == 'POST':
        originalURL = request.POST.get('originalURL')

        existingShortURL = ShortURL.objects(originalURL = originalURL)

        #problem if different users try to shorten same URL -> possibly authentication will take care of it ??
        if len(existingShortURL) > 0:
            return HttpResponse('For specified URL , a shortened URL has already been created')

        methodOfGeneration = request.POST.get('methodOfGeneration')
        modifiedURL = "http://127.0.0.1:8000/"
        if methodOfGeneration == 'manual':
            modifiedURL += request.POST.get('manualShortURL')
        elif methodOfGeneration == 'auto':
            modifiedURL += generateRandomShortUrl(originalURL)

        shortURL = ShortURL(shortURL = modifiedURL,originalURL = originalURL,hitCount = 0)
        shortURL.save()

        return HttpResponse('Your URL has been shortened')

    return HttpResponse("GET Request -> A form , to enter the URL to be shortened , is rendered")
