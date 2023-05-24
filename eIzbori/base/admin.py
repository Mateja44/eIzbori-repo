from django.contrib import admin
from .models import MaticnaSekcija, RegionalniCentar, IzbornaKomisija

# Register your models here.     

admin.site.register(MaticnaSekcija)
admin.site.register(RegionalniCentar)
admin.site.register(IzbornaKomisija)

from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Kandidati
from django import forms
from .models import Kandidati
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

class CsvImportForm(forms.Form):
    csv_upload = forms.FileField()

class KandidatiAdmin(admin.ModelAdmin):
    list_display = ('ime', 'prezime', 'regionalni_centar', 'maticna_sekcija')

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
            
            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = Kandidati.objects.update_or_create(
                    ime = fields[0],
                    prezime = fields[1],
                    regionalni_centar = fields[2],
                    maticna_sekcija = fields[3],
                    )
                
            url = reverse('admin:index')
            return HttpResponseRedirect(url)

        form = CsvImportForm()
        data = {"form": form}
        return render(request, "admin/csv_upload.html", data)

admin.site.register(Kandidati, KandidatiAdmin)