# Generated by Django 4.0.1 on 2022-09-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0006_donar_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='auth_token',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
