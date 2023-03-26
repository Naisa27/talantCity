from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from .models import *

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TrainingAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Trainings
        fields = '__all__'


class InstructorsAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Instructors
        fields = '__all__'


class ArticlesAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Articles
        fields = '__all__'


class ShedulersAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Shedulers
        fields = '__all__'

@admin.register(TrainingTypes)
class TrainingTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("name", "url", )
    search_fields = ("name", )

@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url", "get_image", )
    readonly_fields = ("get_image",)
    list_display_links = ("name", "url", )
    search_fields = ("name", )
    fieldsets = (
        (None, {
            "fields": (("name", "url", ), ),
        }),
        (None, {
            "fields": (("description", "image", "get_image", ),),
        }),
    )

    def get_image( self, obj ):
        return mark_safe(f'<img src={obj.image.url} width="auto", height="50"')

    get_image.short_description = "Изображение"

@admin.register(Genders)
class GenderAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("name", )

@admin.register(Instructors)
class InstructorsAdmin(admin.ModelAdmin):
    list_display = ("id", "fio", "gender", "birthday", "education", "url", "get_image" )
    list_display_links = ("fio", )
    list_filter = ("gender", "education")
    search_fields = ("fio", )
    readonly_fields = ("get_image",)
    form = InstructorsAdminForm
    fieldsets = (
        (None, {
            "fields": (("fio", "gender", "birthday",),),
        }),
        (None, {
            "fields": (("education", "description", ),),
        }),
        (None, {
            "fields": (("locality", "image", "get_image", "url",),),
        }),
        ('Контакты', {
            "fields": (("email", "mobphone", "vk", "tg",),),
        }),
    )

    def get_image( self, obj ):
        return mark_safe(f'<img src={obj.image.url} width="auto", height="50"')

    get_image.short_description = "Фото"

class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email", )

@admin.register(Trainings)
class TrainingsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "trainingType", "dtStart", "dtEnd", "locality", "url", "get_image", "draft")
    list_display_links = ("name", )
    list_filter = ("trainingType", "locality")
    search_fields = ("name", )
    inlines = [ReviewInline]
    save_on_top = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    form = TrainingAdminForm
    actions = ["publish", "unpublish"]
    #fields = (("dtStart", "dtEnd", ), ("locality", "instructors",)) #позволяет показать или не показать поля,
    # а также группировать
    fieldsets = (
        (None, {
            "fields": ( ("name", "trainingType", ), ),
        }),
        (None, {
            "fields": ( ("dtStart", "dtEnd", "image", "get_image", ), ),
        }),
        (None, {
            "fields": (("locality", "instructors", ), ),
        }),
        ("Oписание", {
            "classes": ("collapse", ),
            "fields": (("shortText", "description", ), ),
        }),
        ("Опции", {
            "fields": (("url", "draft", ), ),
        }),
    )
    #save_as = True #переделывает кнопку "сохранить и добавить другой объект" на кнопку "сохранить как новый объект"

    def get_image( self, obj ):
        return mark_safe(f'<img src={obj.image.url} width="auto", height="50"')

    def unpublish( self, request, queryset ):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish( self, request, queryset ):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permission = ('change',)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permission = ('change',)

    get_image.short_description = "Изображение"

@admin.register(Shedulers)
class ShedulersAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "training", "dtStart", "dtEnd", "dtChange",)
    list_display_links = ("name", )
    list_filter = ("training", "dtStart")
    form = ShedulersAdminForm
    fieldsets = (
        (None, {
            "fields": (("training", ),),
        }),
        (None, {
            "fields": (("name", "dtStart", "dtEnd",),),
        }),
        (None, {
            "fields": ("description", "instructors",),
        }),
    )

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "parent", "training", "article",)
    list_display_links = ("name", )
    list_filter = ("training", "article")
    search_fields = ("name", "email", )
    readonly_fields = ("name", "email", )
    fieldsets = (
        (None, {
            "fields": (("name", "email",),),
        }),
        (None, {
            "fields": (("parent", "text", ),),
        }),
        (None, {
            "fields": (("training", "article",),),
        }),
    )

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "dtInsert", "dtChange", "url", "get_image", "draft",)
    list_display_links = ("name", )
    list_filter = ("dtInsert",)
    search_fields = ("name", )
    inlines = [ReviewInline]
    list_editable = ("draft",)
    readonly_fields = ("get_image", )
    form = ArticlesAdminForm
    actions = ['publish', 'unpublish']
    fieldsets = (
        (None, {
            "fields": (("name", "url", "image", "get_image", ),),
        }),
        (None, {
            "fields": (("dtInsert", "dtChange",),),
        }),
        (None, {
            "fields": (("description", "draft",),),
        }),
    )

    def get_image( self, obj ):
        return mark_safe(f'<img src={obj.image.url} width="auto", height="50"')

    def unpublish( self, request, queryset ):
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    def publish( self, request, queryset ):
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    publish.allowed_permission = ('change',)

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permission = ('change',)

    get_image.short_description = "Изображение"


admin.site.site_title = "Админка сайта Станислава Мюллера"
admin.site.site_header = "Админка сайта Станислава Мюллера"