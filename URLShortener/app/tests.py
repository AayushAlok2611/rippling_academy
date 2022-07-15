from django.test import TestCase,Client
from .models import ShortURL
from users.models import User
from mongoengine import *

# Create your tests here.    
class ShortenURL(TestCase):
    # Useful link
    # https://stackoverflow.com/questions/48918354/testing-django-with-mongoengine
    def _fixture_setup(self):
        pass
    def _fixture_teardown(self):
        pass
    def setUp(self) :
        self.client = Client()

    def test_get_home_view(self):
        #Dummy user
        User(username='DummyPresentUser',password="1234567890").save()

        #testing for unauthenticated request to URL
        response1 = self.client.get('/home')
        self.assertEqual(response1.status_code,200)
        self.assertEqual(response1.content.decode(),'Not authenticated to access this URL')

        #testing for authenticated request to URL
        response2 = self.client.get('/home',**{'username':'DummyPresentUser'})
        self.assertEqual(response2.status_code,200)
        self.assertEqual(response2.content.decode(),'GET Request -> A form , to enter the URL to be shortened , is rendered')

        #deleting dummy user
        User.objects(username="DummyPresentUser")[0].delete()

    
    def test_post_home_view(self):

        ShortURL(shortURL = "short.ly/ncg-2022" , originalURL = "google.com" , hitCount = 0).save()

        #handling case when originalURL already shortend and methodOfGeneration = auto
        response1 = self.client.post('/home',{'originalURL':'google.com','methodOfGenration':'auto'})
        self.assertEqual(response1.status_code,200)
        self.assertEqual(response1.content.decode(),'For specified URL , a shortened URL has already been created')

        #handling case when originalURL already shortend and methodOfGeneration = manual
        response2 = self.client.post('/home',{'originalURL':'google.com','methodOfGenration':'manual' , 'manualShortURL':'ncg-2022' })
        self.assertEqual(response2.status_code,200)
        self.assertEqual(response2.content.decode(),'For specified URL , a shortened URL has already been created')

        #handling case when originalURL not yet shortend and methodOfGeneration = auto
        response3 = self.client.post('/home',{'originalURL':'bing.com','methodOfGenration':'auto'})
        self.assertEqual(response3.status_code,200)
        self.assertEqual(response3.content.decode(),'Your URL has been shortened')

        #handling case when originalURL already shortend and methodOfGeneration = manual
        response4 = self.client.post('/home',{'originalURL':'yahoo.com','methodOfGenration':'manual' , 'manualShortURL':'ncg-2022' })
        self.assertEqual(response4.status_code,200)
        self.assertEqual(response4.content.decode(),'Your URL has been shortened')

        #delete the unnecessarily created ShortURLs
        ShortURL.objects(originalURL = "google.com").delete()
        ShortURL.objects(originalURL = "bing.com").delete()
        ShortURL.objects(originalURL = "yahoo.com").delete()        