from django.shortcuts import render
from django.views.generic.base import View
from .models import *


class TrainingsView(View):
    def get(self, request):
        trainings = Trainings.objects.all()
        return render(request, "sam/index.html", {"training_list": trainings, "trainings_count": range(trainings.count())})

