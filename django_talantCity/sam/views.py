from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import *


class TrainingsView(ListView):
    model = Trainings
    queryset = Trainings.objects.filter(draft=False)
    template_name = "sam/index.html"


class TrainingDetailView(DetailView):
    model = Trainings
    slug_field = "url"
    context_object_name = "training"
    # sheduler = Shedulers.objects.filter(training_id=training.id)
    template_name = "sam/training_detail.html"

