# Generated by Django 4.1.6 on 2023-03-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0017_trainings_shorttext_alter_reviews_dtinsert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainings',
            name='shortText',
            field=models.TextField(max_length=255, null=True, verbose_name='Краткое описание'),
        ),
    ]
