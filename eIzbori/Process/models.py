from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin  
from django.conf import settings
from django.utils.translation import gettext_lazy as _   
from simple_history.models import HistoricalRecords

    
class CustomUser(AbstractUser,PermissionsMixin):
 
    
    username = None
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=200,unique=True)
    licence = models.CharField(max_length=50)

    CHOICES = (
    (0, 'Candidacy Phase'),
    (1, 'Voting Phase'),
    (2, 'Election Over')
    ) 

    votestatus = models.IntegerField(choices = CHOICES)

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

    # TODO change ballot model, remove voter field, replace with different way of keeping track of who voted for each phase.
class ballot(models.Model):
    # voter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="voter") # defines who placed the vote
    votes = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="votes") # defines who the vote is for
    votetype = models.BooleanField() #determines whether the vote is placed for candidacy (False) or final voting (True) if user does NOT have a vote for current votetype then they can vote.
    history = HistoricalRecords() #a field that allows lookup of previous versions of the model
    

    #### IMPORTANT!!!! ####
    # No, Django Simple History will not work with instances that were deleted by deleting the entire table. When you delete a table, all records and their corresponding history records (if using Django Simple History) are permanently removed from the database.
    # Django Simple History relies on the Django ORM and database triggers to capture changes to model instances. When you delete a table, the triggers associated with that table, which are responsible for recording history, are also removed.
    # To benefit from the history tracking provided by Django Simple History, you need to delete individual instances using the ORM's delete() method or another appropriate method. Deleting individual instances triggers the necessary mechanisms to record the deletion in the history log.
    # If you delete the entire table, you will lose the ability to retrieve the history of the deleted instances using Django Simple History.

class election(models.Model):
    CHOICES = (
        (0, 'Candidacy Phase'),
        (1, 'Voting Phase'),
        (2, 'Election Over')
    )   # this gives us the possible values for the "Phase" field, which will determine which phase we are in, in the election process. This will be important later when checking which phase we are in in several functions, and is a field we will change throughout each step of the election process.
    date = models.DateTimeField()
    name_of_election = models.CharField(max_length=50)
    Phase = models.IntegerField(choices=CHOICES)


class key_of(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=20)