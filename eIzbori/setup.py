import csv,sys, os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eIzbori.settings')
django.setup()
from django.conf import settings

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from Process.models import *


project_dir = "eIzbori/Process"
sys.path.append(project_dir)


file = "Resources/Sheet1.csv"
data = csv.reader(open(file),delimiter =",")
finlist = {}
for row in data:
    if row[0] != "Name":
        if row[2]  not in finlist:
            finlist[row[2]] = []
        if row[3] not in finlist[row[2]]:
            finlist[row[2]].append(row[3])

# populates database with local and regional centers and links them together
list = list(dict.keys(finlist))
for item in list:
    reg = regional_center()
    reg.name = item
    reg.save()
    for center in finlist[item]:
        loc = local_center()
        loc.name = center
        loc.regional_center = reg
        loc.save()
     
     
#fills is_within table  with user and local center id's upon user generation.
data = csv.reader(open(file),delimiter =",")
Usermodel = get_user_model()
for row in data:
    if row[0] != "Name":
        model = Usermodel()
        model.first_name = row[0]
        model.set_password(raw_password=row[4])
        model.email = row[5]
        model.save()
        localcent = row[3]
    
        isw = is_within()
        isw.user = model
        print(localcent)
        isw.local_center = local_center.objects.get(name = localcent)
        isw.save()









# userlist = []
# passlist = []
# for row in data:
#     if row[0] != "Name":
#         userlist.append(row[0])
#         passlist.append(row[4])

# for x in range(len(userlist)):
#     user = User.objects.create_user(username=f"{str(userlist[x])}",
#                                     password='what')
#     user.save()

#  # WHY WONT THIS FUCKING WORK!?!?!
#     # user = User.objects.create_user(username=f"{str(row[0])}",
#     #                                 password=f'{str(row[4])}')
    


# isw = is_within()




