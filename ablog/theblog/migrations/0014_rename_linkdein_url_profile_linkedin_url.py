# Generated by Django 3.2 on 2021-06-03 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_rename_pinterest_url_profile_linkdein_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='linkdein_url',
            new_name='linkedin_url',
        ),
    ]
