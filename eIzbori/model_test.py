import csv,sys, os, django,datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eIzbori.settings')
django.setup()
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Process.models import *

user = CustomUser.objects.get(first_name = "Pat")
print(is_within.objects.get(user = user).local_center.name)

instance = is_within.objects.get(user=user)
snapshot = instance.history.as_of(datetime.datetime.now())
print(snapshot)

fields = snapshot._meta.fields


# Print field names and their corresponding values
for field in fields:
    field_name = field.name
    field_value = getattr(snapshot, field_name)
    print(f"{field_name}: {field_value}")