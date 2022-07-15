from telnetlib import DO
from django.db import models
from mongoengine import *


# Create your models here.
class ShortURL(Document):
    shortURL = StringField(max_length=None)
    originalURL = StringField(max_length=None)
    hitCount = IntField()
    lastHit = DateTimeField()

