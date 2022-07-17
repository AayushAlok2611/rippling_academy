from telnetlib import DO
from django.db import models
from mongoengine import *
from users.models import User

# Create your models here.
class ShortURL(Document):
    shortURL = StringField(max_length=None)
    originalURL = StringField(max_length=None)
    hitCount = IntField()
    lastHit = DateTimeField()
    user = ReferenceField(User,reverse_delete_rule=CASCADE)


