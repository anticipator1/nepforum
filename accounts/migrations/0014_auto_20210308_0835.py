# Generated by Django 3.1.6 on 2021-03-08 02:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_addcomment_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addcomment',
            name='forum_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.forum_users'),
        ),
    ]