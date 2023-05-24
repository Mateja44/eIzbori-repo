import csv,sys, os, django
from eIzbori import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eIzbori.settings')
django.setup()




from Process.models import *

info = local_center.objects.get(name = "section 0a")
print(info.regional_center.name)