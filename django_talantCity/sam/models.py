from datetime import date, datetime
# import datetime

from django.db import models
from django.urls import reverse


class TrainingTypes(models.Model):
    name = models.CharField("Тип тренинга", max_length=200)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=255, unique=True, default="q")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "тип тренинга"
        verbose_name_plural = "типы тренинга"


class Locality(models.Model):
    name = models.CharField("Место тренинга", max_length=255)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="locality")
    url = models.SlugField(max_length=255, unique=True, default="q")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "место проведения тренинга"
        verbose_name_plural = "места проведения тренингов"


class Genders(models.Model):
    name = models.CharField("Пол", max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "пол"
        verbose_name_plural = "пол"


class Instructors(models.Model):
    fio = models.CharField("ФИО", max_length=255)
    gender = models.ForeignKey(
        Genders, verbose_name="пол", on_delete=models.SET_NULL, null=True
    )
    birthday = models.DateField("Дата рождения")
    education = models.CharField("Образование", max_length=255)
    description = models.TextField("Описание", null=True)
    image = models.ImageField("Изображение", upload_to="instructors")
    locality = models.ManyToManyField(
        Locality, verbose_name="места проведения тренингов", related_name="instructor_locality"
    )
    url = models.SlugField(max_length=255, unique=True, default="q")
    email = models.EmailField("e-mail", max_length=254, null=True)
    mobphone = models.CharField("Телефон", max_length=254, null=True )
    vk = models.URLField("страница ВК", max_length=254, null=True)
    tg = models.URLField("страница Telegramm", max_length=254, null=True)

    def __str__(self):
        return self.fio

    def get_absolute_url( self ):
        return reverse('instructor_detail', kwargs={"slug": self.url})

    def get_age( self ):
        return date.today().year - self.birthday.year
        # return 25


    class Meta:
        verbose_name = "тренер"
        verbose_name_plural = "тренеры"


class Trainings(models.Model):
    name = models.CharField("Название", max_length=255)
    trainingType = models.ForeignKey(
        TrainingTypes, verbose_name="тип тренинга", on_delete=models.SET_NULL, null=True
    )
    dtStart = models.DateField("дата начала", default=date.today)
    dtEnd = models.DateField("дата завершения", default=date.today)
    locality = models.ForeignKey(
        Locality, verbose_name="место проведения тренинга", on_delete=models.SET_NULL, null=True
    )
    instructors = models.ManyToManyField(
        Instructors, verbose_name="тренеры", related_name="traning_instructor"
    )
    draft = models.BooleanField("Черновик", default=False)
    url = models.SlugField(max_length=255, unique=True)
    image = models.ImageField("Изображение", upload_to="trainings", null=True)
    description = models.TextField("Описание", null=True)
    shortText = models.TextField("Краткое описание", max_length=255, null=True )

    def __str__(self):
        return self.name

    def get_short_description( self ):
        return self.shortText

    def get_absolute_url(self):
        return reverse("training_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "тренинг"
        verbose_name_plural = "тренинги"


class Shedulers(models.Model):
    name = models.CharField("название", max_length=100, null=True)
    training = models.ForeignKey(
        Trainings, verbose_name="тренинг", on_delete=models.CASCADE
    )
    dtChange = models.DateTimeField("изменено", auto_now_add=True)
    dtStart = models.DateTimeField("дата начала")
    dtEnd = models.DateTimeField("дата завершения")
    description = models.TextField("описание")
    instructors = models.ManyToManyField(
        Instructors, verbose_name="тренеры", related_name="traning_part_instructor", null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "расписание"
        verbose_name_plural = "расписания"


class Articles(models.Model):
    name = models.CharField("Название", max_length=255)
    description = models.TextField("Описание", null=True)
    dtInsert = models.DateField("дата добавления", auto_now_add=True)
    dtChange = models.DateField("дата изменения", default=date.today,)
    draft = models.BooleanField("Черновик", default=False)
    url = models.SlugField(max_length=255, unique=True)
    image = models.ImageField("Изображение", upload_to="articles", null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=250)
    text = models.TextField("Сообщение")
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    training = models.ForeignKey(
        Trainings, verbose_name="Тренинг", on_delete=models.SET_NULL, blank=True, null=True
    )
    article = models.ForeignKey(
        Articles, verbose_name="Статья", on_delete=models.SET_NULL, blank=True, null=True
    )
    dtInsert = models.DateTimeField("дата изменения", auto_now_add=True, null=True, )

    def __str__(self):
        return f"{self.name} - {self.training}"

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"
