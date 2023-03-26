
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import *
import datetime

from .forms import ReviewForm

class trainingTypesLocalities():
    def get_trainingTypes( self ):
        return TrainingTypes.objects.all()

    def get_trainingLocalities( self ):
        return Locality.objects.order_by("name")

class TrainingsView(ListView):
    model = Trainings
    queryset = Trainings.objects.filter(draft=False)
    template_name = "sam/index.html"


# class TrainingsListView(ListView):
#     model = Trainings
#     context_object_name = "trainings_list"
#     queryset = Trainings.objects.filter(draft=False)
#     template_name = "sam/trainings_list.html"


class TrainingDetailView(DetailView):
    model = Trainings
    slug_field = "url"
    context_object_name = "training"
    # sheduler = Shedulers.objects.filter(training_id=training.id)
    template_name = "sam/training_detail.html"


class InstructorDetailView(DetailView):
    model = Instructors
    slug_field = "url"
    context_object_name = "instructor"
    template_name = "sam/instructor.html"



class AddReview(View):
    def post( self, request, pk ):
        form = ReviewForm(request.POST)

        page_id = Trainings.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))

            form.training = page_id
            form.save()
        return redirect(page_id.get_absolute_url())


class FilterTrainingsView(ListView):
    template_name = "sam/index.html"
    model = Trainings
    # queryset = Trainings.objects.filter(
    #         Q(locality__in=HttpRequest.GET.get("locality")) |
    #         Q(trainingType__in=HttpRequest.GET.get("trainingType"))
    #     )

    def get_queryset(self):
        queryset = Trainings.objects.filter(
            Q(locality__in=self.request.GET.getlist("locality")) |
            Q(trainingType__in=self.request.GET.getlist("trainingType"))
        )
        return queryset
