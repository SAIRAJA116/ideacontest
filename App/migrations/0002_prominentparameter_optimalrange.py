# Generated by Django 3.2.12 on 2022-03-16 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prominentparameter',
            name='optimalrange',
            field=models.CharField(default=' ', max_length=300),
        ),
    ]