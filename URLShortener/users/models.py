from django.db import models
from mongoengine import *
import mongoengine

# Create your models here.
class User(Document):
    username = StringField()
    password = StringField()

