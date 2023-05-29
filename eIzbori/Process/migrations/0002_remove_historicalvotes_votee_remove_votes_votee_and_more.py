# Generated by Django 4.2.1 on 2023-05-26 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Process', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalvotes',
            name='votee',
        ),
        migrations.RemoveField(
            model_name='votes',
            name='votee',
        ),
        migrations.AddField(
            model_name='votes',
            name='votee',
            field=models.ManyToManyField(related_name='votee', to=settings.AUTH_USER_MODEL),
        ),
    ]