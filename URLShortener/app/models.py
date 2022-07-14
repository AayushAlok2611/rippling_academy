from telnetlib import DO
from django.db import models
from mongoengine import *

# Create your models here.
class ShortURL(EmbeddedDocument):
    shortURL = StringField(max_length=None)
    originalURL = StringField(max_length=None)
    hitCount = IntField()
    lastHit = DateTimeField()

class User(Document):
    username = StringField()
    password = StringField()
    shortURLs = ListField(EmbeddedDocumentField(ShortURL))

