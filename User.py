import datetime
import peewee
from peewee import *

from sql import db


class User(peewee.Model):
    email = CharField()
    status = BooleanField(default=True)
    firstname = CharField()
    lastname = CharField()
    age = IntegerField()
    created = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db
