# Generated by Django 4.1.2 on 2022-11-23 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_rename_avatar_personalinfo_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinfo',
            name='profile_pic',
        ),
    ]
