# Generated by Django 4.1.6 on 2023-02-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0002_trainingtypes_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructors',
            name='url',
            field=models.SlugField(default='q', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='locality',
            name='url',
            field=models.SlugField(default='q', max_length=255, unique=True),
        ),
    ]