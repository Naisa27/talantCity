# Generated by Django 4.1.6 on 2023-02-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0007_alter_shedulers_dtend_alter_shedulers_dtstart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shedulers',
            name='instructors',
            field=models.ManyToManyField(null=True, related_name='traning_part_instructor', to='sam.instructors', verbose_name='тренеры'),
        ),
    ]
