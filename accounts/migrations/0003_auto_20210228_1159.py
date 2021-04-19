# Generated by Django 3.1.6 on 2021-02-28 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='forum_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.forum_users'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('hacking', 'hacking'), ('tech', 'tech'), ('music', 'music')], max_length=200, null=True),
        ),
    ]