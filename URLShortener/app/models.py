from telnetlib import DO
from django.db import models
from mongoengine import *
import mongoengine


# Create your models here.
class ShortURL(Document):
    shortURL = StringField(max_length=None)
    originalURL = StringField(max_length=None)
    hitCount = IntField()
    lastHit = DateTimeField()

class User(Document):
    username = StringField()
    password = StringField()
    shortURLs = ListField(ReferenceField(ShortURL,reverse_delete_rule = mongoengine.PULL))

