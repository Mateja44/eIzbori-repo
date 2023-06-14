from .models import CustomUser
from django.db.models import Count

column_count = CustomUser.objects.aggregate(count=Count('licence'))
size = len(column_count)
print(size)