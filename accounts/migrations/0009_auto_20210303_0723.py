# Generated by Django 3.1.6 on 2021-03-03 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210302_2105'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='AddComment',
        ),
    ]