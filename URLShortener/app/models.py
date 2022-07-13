from telnetlib import DO
from django.db import models
from mongoengine import *

# Create your models here.
class UserModel(Document):
    name = StringField(max_length=30,required=True)
    password = StringField(max_length=30,required=True)