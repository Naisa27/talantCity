from django.urls import path
from . import views


urlpatterns = [
    path("", views.TrainingsView.as_view()),
    path("filter/", views.FilterTrainingsView.as_view(), name='filter'),
    path("<slug:slug>/", views.TrainingDetailView.as_view(), name='training_detail'),
    path("review/<int:pk>", views.AddReview.as_view(), name='add_review'),
    path("instructor/<slug:slug>/", views.InstructorDetailView.as_view(), name='instructor_detail'),
    # path("trainings/", views.TrainingsListView.as_view(), name='instructor_detail'),
]
