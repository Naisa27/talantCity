# Generated by Django 4.1.6 on 2023-03-05 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0010_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='training',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.trainings', verbose_name='Тренинг'),
        ),
    ]
