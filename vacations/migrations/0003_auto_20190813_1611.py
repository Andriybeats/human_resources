# Generated by Django 2.2.4 on 2019-08-13 16:11

from django.db import migrations, models
import vacations.validators


class Migration(migrations.Migration):

    dependencies = [
        ('vacations', '0002_auto_20190813_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='date_start',
            field=models.DateField(validators=[vacations.validators.validate_start_date]),
        ),
    ]
