from django.urls import path
from . import views


urlpatterns = [
    path("", views.TrainingsView.as_view()),
]
