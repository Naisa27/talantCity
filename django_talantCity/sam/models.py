from datetime import date

from django.db import models


class TrainingTypes(models.Model):
    name = models.CharField("Тип тренинга", max_length=200)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=255, unique=True, default="q")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип тренинга"
        verbose_name_plural = "Типы тренинга"


class Locality(models.Model):
    name = models.CharField("Место тренинга", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="locality")
    url = models.SlugField(max_length=255, unique=True, default="q")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Место проведения тренинга"
        verbose_name_plural = "Места проведения тренингов"


class Genders(models.Model):
    name = models.CharField("Пол", max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пол"
        verbose_name_plural = "Пол"


class Instructors(models.Model):
    fio = models.CharField("ФИО", max_length=255)
    gender = models.ForeignKey(
        Genders, verbose_name="Пол", on_delete=models.SET_NULL, null=True
    )
    birthday = models.DateField("Дата рождения")
    education = models.CharField("Образование", max_length=255)
    description = models.CharField("Описание", max_length=255)
    image = models.ImageField("Изображение", upload_to="instructors")
    locality = models.ManyToManyField(
        Locality, verbose_name="места проведения тренингов", related_name="instructor_locality"
    )
    url = models.SlugField(max_length=255, unique=True, default="q")

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"


class Trainings(models.Model):
    name = models.CharField("Название", max_length=255)
    trainingType = models.ForeignKey(
        TrainingTypes, verbose_name="Тип тренинга", on_delete=models.SET_NULL, null=True
    )
    dtStart = models.DateField("дата начала", default=date.today)
    dtEnd = models.DateField("дата завершения", default=date.today)
    locality = models.ForeignKey(
        Locality, verbose_name="Место проведения тренинга", on_delete=models.SET_NULL, null=True
    )
    instructors = models.ManyToManyField(
        Instructors, verbose_name="тренеры", related_name="traning_instructor"
    )
    draft = models.BooleanField("Черновик", default=False)
    url = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тренинг"
        verbose_name_plural = "Тренинги"

