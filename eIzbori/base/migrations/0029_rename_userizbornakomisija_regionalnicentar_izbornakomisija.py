# Generated by Django 4.1.4 on 2023-05-24 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_remove_izbornakomisija_maticnasekcija_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regionalnicentar',
            old_name='userizbornakomisija',
            new_name='izbornakomisija',
        ),
    ]
