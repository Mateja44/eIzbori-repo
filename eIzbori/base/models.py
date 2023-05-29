from django.db import models
from django.contrib.auth.models import User

# Create your models here.
  
class IzbornaKomisija(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Izborna Komisija"

class RegionalniCentar(models.Model):
    broj = models.IntegerField(default=0)
    izbornakomisija = models.ForeignKey(IzbornaKomisija, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __int__(self):
        return self.broj
    
    class Meta:
        verbose_name_plural = "Regionalni Centri"
    
class MaticnaSekcija(models.Model):
    regionalnicentar = models.ForeignKey(RegionalniCentar, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.regionalnicentar
    
    class Meta:
        verbose_name_plural = "Maticna Sekcija"
    
class Kandidati(models.Model):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    maticna_sekcija = models.CharField(max_length=100)
    regionalni_centar = models.CharField(max_length=100)
    email = models.EmailField('User Email', blank=False, null=True)

    def __str__(self):
        return self.ime + ' ' + self.prezime
    
    class Meta:
        verbose_name_plural = "Kandidati"

class Izbori(models.Model):
    ime_izbora = models.CharField('Ime Izbora', max_length=100)
    datum = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Izbori"

class Kandidovanje(models.Model):
    kandidati = models.ManyToManyField(Kandidati, blank=False)

    class Meta:
        verbose_name_plural = "Kandidovanje"