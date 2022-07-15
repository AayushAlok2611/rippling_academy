from django.db import models
from mongoengine import *
import mongoengine
from app.models import ShortURL

# Create your models here.
class User(Document):
    username = StringField()
    password = StringField()
    shortURLs = ListField(ReferenceField(ShortURL,reverse_delete_rule = mongoengine.PULL))

