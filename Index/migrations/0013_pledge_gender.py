# Generated by Django 3.1 on 2022-10-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0012_auto_20221010_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]