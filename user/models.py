from django.db import models
from quiz_backend.connection_db import db

# Create your models here.
user_collection = db['User']

class User:
    def __init__(self, _id = None, name = None, email = None, password = None):
        self._id = _id
        self.name = name
        self.email = email
        self.password = password
    
    