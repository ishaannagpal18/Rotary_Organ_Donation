# Generated by Django 4.0.1 on 2022-09-21 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0009_pledge_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledge',
            name='user',
        ),
    ]
