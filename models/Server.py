from mongoengine import *
import datetime

class Team(Document):
    name = StringField(required=True)
    base_loc = StringField()
    members = ListField(IntField())

class Server(Document):
    name = StringField(required=True, unquie=True)
    teams = ListField(ReferenceField(Team), default=[])
    created_at = DateTimeField(default=datetime.datetime.now)
    