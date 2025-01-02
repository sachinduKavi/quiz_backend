from django.db import models

# Create your models here.
class User(models.Model):
    user_ID = models.AutoField(primary_key=True, auto_created=True)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name