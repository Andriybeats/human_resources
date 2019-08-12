# Generated by Django 2.2.4 on 2019-08-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='abbreviation',
            field=models.CharField(max_length=3, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]