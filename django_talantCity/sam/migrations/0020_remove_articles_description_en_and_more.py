# Generated by Django 4.1.6 on 2023-03-25 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0019_articles_description_en_articles_description_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='articles',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='education_en',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='education_ru',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='fio_en',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='fio_ru',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='gender_en',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='gender_ru',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='locality_en',
        ),
        migrations.RemoveField(
            model_name='instructors',
            name='locality_ru',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='text_en',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='shedulers',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='shedulers',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='shedulers',
            name='instructors_en',
        ),
        migrations.RemoveField(
            model_name='shedulers',
            name='instructors_ru',
        ),
        migrations.RemoveField(
            model_name='shedulers',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='shedulers',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='shedulers',
            name='training_en',
        ),
        migrations.RemoveField(
            model_name='shedulers',
            name='training_ru',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='instructors_en',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='instructors_ru',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='locality_en',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='locality_ru',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='shortText_en',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='shortText_ru',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='trainingType_en',
        ),
        migrations.RemoveField(
            model_name='trainings',
            name='trainingType_ru',
        ),
        migrations.RemoveField(
            model_name='trainingtypes',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='trainingtypes',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='trainingtypes',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='trainingtypes',
            name='name_ru',
        ),
    ]
