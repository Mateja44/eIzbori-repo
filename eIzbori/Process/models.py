from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin  
from django.conf import settings
from django.utils.translation import gettext_lazy as _   
from simple_history.models import HistoricalRecords
# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(max_length = 200,unique = True)
#     password = models.CharField(max_length= 40)
#     def __str__(self):
#         return self.email
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
    
class CustomUser(AbstractUser,PermissionsMixin):
    username = None
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=200,unique=True)
    licence = models.CharField(max_length=50)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class regional_center(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class local_center(models.Model):
    name = models.CharField(max_length=40)
    regional_center = models.ForeignKey(regional_center,on_delete=models.CASCADE)

class is_within(models.Model):
    local_center = models.ForeignKey(local_center, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    history = HistoricalRecords()

class votes(models.Model):
    voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="voter") # defines who placed the vote
    votee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votee") # defines who the vote is for
    votetype = models.BooleanField() #determines whether the vote is placed for candidacy (False) or final voting (True)
    history = HistoricalRecords()

class election(models.Model):
    date = models.DateTimeField()
    name_of_election = models.CharField(max_length=50)