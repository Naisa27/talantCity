from django import template
from django.http import HttpRequest, request, QueryDict

from ..models import TrainingTypes, Reviews, Locality, Trainings

register = template.Library()

@register.simple_tag()
def get_trainingTypes():
    return TrainingTypes.objects.all()

@register.simple_tag()
def get_trainingLocalities():
    return Locality.objects.order_by("name")


@register.inclusion_tag('include/reviews.html')
def get_reviews_training(training):
    reviews = Reviews.objects.filter(training_id=training, parent__isnull=True).order_by("-dtInsert")
    return {
        "reviews": reviews,
        'id': training,
    }

@register.inclusion_tag('sam/trainings_list.html')
def get_trainings_list(queryset):
    # print('queryset = ', QueryDict.getlist("locality"))

    trainings = Trainings.objects.filter(draft=False)
    return {
        "trainings": queryset if queryset else trainings,
    }


@register.inclusion_tag('include/reviews.html')
def training_review(id, context, page):
    return {
        'id': id,
        'context': context,
        'page': page,
    }

@register.inclusion_tag('include/article.html')
def article_review(id, context, page):
    return {
        'id': id,
        'context': context,
        'page': page,
    }

