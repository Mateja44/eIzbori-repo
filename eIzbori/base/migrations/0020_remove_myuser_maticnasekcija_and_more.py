# Generated by Django 4.1.4 on 2023-05-23 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_kandidati'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='maticnasekcija',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='regionalnicentar',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='regionalnicentar',
            name='user',
        ),
        migrations.RemoveField(
            model_name='kandidati',
            name='maticnasekcija',
        ),
        migrations.RemoveField(
            model_name='kandidati',
            name='regionalnicentar',
        ),
        migrations.DeleteModel(
            name='MaticnaSekcija',
        ),
        migrations.DeleteModel(
            name='MyUser',
        ),
        migrations.DeleteModel(
            name='RegionalniCentar',
        ),
    ]
