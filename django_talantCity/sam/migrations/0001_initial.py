# Generated by Django 4.1.6 on 2023-02-07 21:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Пол',
                'verbose_name_plural': 'Пол',
            },
        ),
        migrations.CreateModel(
            name='Instructors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=255, verbose_name='ФИО')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('education', models.CharField(max_length=255, verbose_name='Образование')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('image', models.ImageField(upload_to='instructors', verbose_name='Изображение')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.genders', verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренеры',
            },
        ),
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Место тренинга')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='locality', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Место проведения тренинга',
                'verbose_name_plural': 'Места проведения тренингов',
            },
        ),
        migrations.CreateModel(
            name='TrainingTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Тип тренинга')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тип тренинга',
                'verbose_name_plural': 'Типы тренинга',
            },
        ),
        migrations.CreateModel(
            name='Trainings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('dtStart', models.DateField(default=datetime.date.today, verbose_name='дата начала')),
                ('dtEnd', models.DateField(default=datetime.date.today, verbose_name='дата завершения')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('instructors', models.ManyToManyField(related_name='traning_instructor', to='sam.instructors', verbose_name='тренеры')),
                ('locality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.locality', verbose_name='Место проведения тренинга')),
                ('trainingType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.trainingtypes', verbose_name='Тип тренинга')),
            ],
            options={
                'verbose_name': 'Тренинг',
                'verbose_name_plural': 'Тренинги',
            },
        ),
        migrations.AddField(
            model_name='instructors',
            name='locality',
            field=models.ManyToManyField(related_name='instructor_locality', to='sam.locality', verbose_name='места проведения тренингов'),
        ),
    ]
