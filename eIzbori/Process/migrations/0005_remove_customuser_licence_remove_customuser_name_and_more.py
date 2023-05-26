# Generated by Django 4.1.6 on 2023-05-25 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Process', '0004_customuser_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='licence',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
