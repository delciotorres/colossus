# Generated by Django 2.0.6 on 2018-06-11 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_auto_20180611_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglist',
            name='contact_email_address',
            field=models.EmailField(blank=True, max_length=254, verbose_name='contact email address'),
        ),
    ]