from django.test import TestCase,Client
from django.test.runner import DiscoverRunner

# class NoSQLTestRunner(DiscoverRunner):
#     def setup_databases(self, **kwargs):
#         pass
#     def teardown_databases(self, old_config, **kwargs):
#         pass
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
    
    def test_signup_get(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code,200)
    
    def test_login_post(self):
        response = self.client.post('/login',{'username':'Aayush','password':'123'})
        self.assertEqual(response.status_code,200)

    def test_signup_post(self):
        response = self.client.post('/signup',{'username':'Aayush','password':'123'})
        self.assertEqual(response.status_code,200)

    

