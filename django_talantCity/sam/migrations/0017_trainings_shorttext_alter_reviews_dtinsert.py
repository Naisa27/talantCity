# Generated by Django 4.1.6 on 2023-03-23 12:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0016_alter_trainings_dtend_alter_trainings_dtstart'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainings',
            name='shortText',
            field=models.CharField(max_length=255, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='dtInsert',
            field=models.DateTimeField(default=datetime.datetime.today, null=True, verbose_name='дата изменения'),
        ),
    ]
