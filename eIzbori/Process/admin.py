from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import regional_center, local_center, is_within, ballot, election, key_of, CustomUser
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
import csv

admin.site.register(regional_center)
admin.site.register(local_center)
admin.site.register(is_within)
admin.site.register(ballot)
admin.site.register(election)
admin.site.register(key_of)

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class CustomUserAdmin(UserAdmin): #admin.ModelAdmin:
    list_display = ['email', 'licence']
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'password', 'sifra', 'email', 'licence', 'regional_section', 'local_section')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [path('upload-csv/', self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]
            
            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)
            
            csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            next(csv_data)  # Skip the first row (header row) 
            first_line = csv_file.readline().decode("utf-8")
            column_count = first_line.count(',') + 1
            
            #file_data = csv_file.read().decode("utf-8")
            #csv_data = file_data.split("\n")

            for fields in csv_data:
            #fields = x.split(",")
                if len(fields) >= column_count:
                    email = fields[5] 
                    existing_user = CustomUser.objects.filter(email=email)
                    if existing_user.exists():
                        continue

                    created = CustomUser.objects.create(
                    first_name = fields[0],
                    last_name = fields[1],
                    email = fields[5],
                    licence = fields[4],
                    regional_section = fields[2],
                    local_section = fields[3],
                    sifra = fields[6],
                    )

            # for fields in csv_data:
            #     #fields = x.split(",")
            #     if len(fields) >= column_count:
            #         created = CustomUser.objects.update_or_create(
            #         first_name = fields[0],
            #         last_name = fields[1],
            #         email = fields[5],
            #         licence = fields[4],
            #         regional_section = fields[2],
            #         local_section = fields[3],
            #         sifra = fields[6],
            #         )

            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(CustomUser, CustomUserAdmin)
