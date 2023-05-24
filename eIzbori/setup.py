import csv,sys, os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eIzbori.settings')
django.setup()




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
     
     # TODO put within is_within model while generating
     




