# Generated by Django 3.2.13 on 2022-07-02 15:17

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(default='GB', max_length=2),
        ),
    ]
