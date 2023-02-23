# Generated by Django 4.1.6 on 2023-02-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0005_trainings_image_shedulers'),
    ]

    operations = [
        migrations.AddField(
            model_name='shedulers',
            name='name',
            field=models.CharField(max_length=100, null=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='shedulers',
            name='description',
            field=models.TextField(verbose_name='описание'),
        ),
        migrations.AlterField(
            model_name='trainings',
            name='image',
            field=models.ImageField(null=True, upload_to='trainings', verbose_name='Изображение'),
        ),
    ]
