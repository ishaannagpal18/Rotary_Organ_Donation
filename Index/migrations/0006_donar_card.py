# Generated by Django 4.0.1 on 2022-09-20 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0005_pledge_witness1_sign_pledge_witness2_sign'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donar_card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, max_length=100)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Index.pledge')),
            ],
        ),
    ]