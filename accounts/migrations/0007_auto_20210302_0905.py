# Generated by Django 3.1.6 on 2021-03-02 03:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_forum_users_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum_users',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='forum_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.forum_users'),
        ),
    ]
