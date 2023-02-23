from django.urls import path
from . import views


urlpatterns = [
    path("", views.TrainingsView.as_view()),
    path("<slug:slug>/", views.TrainingDetailView.as_view(), name='training_detail'),
]
