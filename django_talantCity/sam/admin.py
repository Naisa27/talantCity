from django.contrib import admin
from .models import TrainingTypes, Locality, Genders, Instructors, Trainings

admin.site.register(TrainingTypes)
admin.site.register(Locality)
admin.site.register(Genders)
admin.site.register(Instructors)
admin.site.register(Trainings)