# Generated by Django 4.1.6 on 2023-03-21 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0014_instructors_email_instructors_mobphone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainings',
            name='dtEnd',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='дата завершения'),
        ),
        migrations.AlterField(
            model_name='trainings',
            name='dtStart',
            field=models.DateTimeField(default=datetime.datetime.today, verbose_name='дата начала'),
        ),
    ]
