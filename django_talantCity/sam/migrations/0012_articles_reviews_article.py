# Generated by Django 4.1.6 on 2023-03-11 08:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0011_alter_reviews_training'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('dtInsert', models.DateField(default=datetime.date.today, verbose_name='дата добавления')),
                ('dtChange', models.DateField(default=datetime.date.today, verbose_name='дата изменения')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('url', models.SlugField(max_length=255, unique=True)),
                ('image', models.ImageField(null=True, upload_to='articles', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
        migrations.AddField(
            model_name='reviews',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.articles', verbose_name='Статья'),
        ),
    ]