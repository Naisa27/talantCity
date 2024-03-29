# Generated by Django 4.1.6 on 2023-03-25 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sam', '0018_alter_trainings_shorttext'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='articles',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='articles',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='articles',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='education_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='education_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Образование'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='fio_en',
            field=models.CharField(max_length=255, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='fio_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='gender_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.genders', verbose_name='пол'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='gender_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.genders', verbose_name='пол'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='locality_en',
            field=models.ManyToManyField(null=True, related_name='instructor_locality', to='sam.locality', verbose_name='места проведения тренингов'),
        ),
        migrations.AddField(
            model_name='instructors',
            name='locality_ru',
            field=models.ManyToManyField(null=True, related_name='instructor_locality', to='sam.locality', verbose_name='места проведения тренингов'),
        ),
        migrations.AddField(
            model_name='locality',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='locality',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='locality',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Место тренинга'),
        ),
        migrations.AddField(
            model_name='locality',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Место тренинга'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='name_en',
            field=models.CharField(max_length=250, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='name_ru',
            field=models.CharField(max_length=250, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Сообщение'),
        ),
        migrations.AddField(
            model_name='shedulers',
            name='description_en',
            field=models.TextField(null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='shedulers',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='описание'),
        ),
        migrations.AddField(
            model_name='shedulers',
            name='instructors_en',
            field=models.ManyToManyField(null=True, related_name='traning_part_instructor', to='sam.instructors', verbose_name='тренеры'),
        ),
        migrations.AddField(
            model_name='shedulers',
            name='instructors_ru',
            field=models.ManyToManyField(null=True, related_name='traning_part_instructor', to='sam.instructors', verbose_name='тренеры'),
        ),
        migrations.AddField(
            model_name='shedulers',
            name='name_en',
            field=models.CharField(max_length=100, null=True, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='shedulers',
            name='name_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='shedulers',
            name='training_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sam.trainings', verbose_name='тренинг'),
        ),
        migrations.AddField(
            model_name='shedulers',
            name='training_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sam.trainings', verbose_name='тренинг'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='instructors_en',
            field=models.ManyToManyField(null=True, related_name='traning_instructor', to='sam.instructors', verbose_name='тренеры'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='instructors_ru',
            field=models.ManyToManyField(null=True, related_name='traning_instructor', to='sam.instructors', verbose_name='тренеры'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='locality_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.locality', verbose_name='место проведения тренинга'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='locality_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.locality', verbose_name='место проведения тренинга'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='shortText_en',
            field=models.TextField(max_length=255, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='shortText_ru',
            field=models.TextField(max_length=255, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='trainingType_en',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.trainingtypes', verbose_name='тип тренинга'),
        ),
        migrations.AddField(
            model_name='trainings',
            name='trainingType_ru',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sam.trainingtypes', verbose_name='тип тренинга'),
        ),
        migrations.AddField(
            model_name='trainingtypes',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='trainingtypes',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='trainingtypes',
            name='name_en',
            field=models.CharField(max_length=200, null=True, verbose_name='Тип тренинга'),
        ),
        migrations.AddField(
            model_name='trainingtypes',
            name='name_ru',
            field=models.CharField(max_length=200, null=True, verbose_name='Тип тренинга'),
        ),
    ]
