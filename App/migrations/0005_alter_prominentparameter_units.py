# Generated by Django 3.2.12 on 2022-03-16 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_auto_20220316_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prominentparameter',
            name='units',
            field=models.CharField(max_length=50),
        ),
    ]