from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

#defining custom user class that will allow for more data fields
class CustomUser(AbstractUser):
    is_commision = models.BooleanField(default=False)
    Key = models.CharField(max_length=20, blank = True)
    licence = models.CharField(max_length=20,blank = True)
    pass

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
