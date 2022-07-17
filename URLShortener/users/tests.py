from django.test import TestCase,Client
from .models import User,ShortURL
from mongoengine import *

# Create your tests here.
class UserAndAuth(TestCase):
    # Useful link 
    # https://stackoverflow.com/questions/48918354/testing-django-with-mongoengine
    def _fixture_setup(self):
        pass
    def _fixture_teardown(self):
        pass

    def setUp(self) :
        self.client = Client()      

    def test_login_get(self) :
        response = self.client.get('/login')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content.decode(),"GET Request -> A form will be rendered to login user")
    
    def test_signup_get(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.content.decode(),'GET Request -> A form will be rendered to sign up user')
    
    def test_login_post(self):

        #here this user is being saved in mongoDB 

        User(username='DummyPresentUser',password="1234567890").save()
        
        #handling case when user already present in DB
        response1 = self.client.post('/login',{'username':'DummyPresentUser','password':'1234567890'})
        self.assertEqual(response1.status_code,200)
        self.assertEqual(response1.content.decode(),"DummyPresentUser")

        #handling case when user not present in DB
        response2 = self.client.post('/login',{'username':'DummyAbsentUser','password':'1234567890'})
        self.assertEqual(response2.status_code,200)
        self.assertEqual(response2.content.decode(),"Username or password incorrect")

        #handling case when user present but wrong password passed
        response3 = self.client.post('/login',{'username':'DummyPresentUser','password':'abcd'})
        self.assertEqual(response3.status_code,200)
        self.assertEqual(response3.content.decode(),"Username or password incorrect")

        #deleting dummy user from mongo DB (necessary -> other test of same testCase class wont have access to "DummyPresentUser")
        User.objects(username = 'DummyPresentUser')[0].delete()

    def test_signup_post(self):

        # Create a dummy user
        User(username='DummyPresentUser',password="1234567890").save()

        #handling case when user already exists
        response1 = self.client.post('/signup',{'username':'DummyPresentUser','password':'1234567890'})
        self.assertEqual(response1.status_code,200)
        self.assertEqual(response1.content.decode(),'User already exists')

        #handling case when user dosent exist
        response2 = self.client.post('/signup',{'username':'DummyAbsentUser','password':'1234567890'})
        self.assertEqual(response2.status_code,200)
        self.assertEqual(response2.content.decode(),'DummyAbsentUser')

        # # deleting dummy user from mongo DB (necessary -> other test of same testCase class wont have access to "DummyPresentUser" )
        User.objects(username = 'DummyPresentUser')[0].delete()

        # DummyAbsentUser must be deleted because it had been added to the DB earlier
        User.objects(username = "DummyAbsentUser" )[0].delete()


