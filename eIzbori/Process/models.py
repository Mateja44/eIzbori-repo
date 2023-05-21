from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#defining custom user class that will allow for more data fields
class CustomUser(AbstractUser):
    is_commision = models.BooleanField(default=False)
    Key = models.CharField(max_length=20, blank = True)
    licence = models.CharField(max_length=20,blank = True)
    pass