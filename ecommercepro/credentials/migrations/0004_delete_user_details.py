# Generated by Django 3.2.13 on 2022-06-05 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0003_user_details_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_details',
        ),
    ]
