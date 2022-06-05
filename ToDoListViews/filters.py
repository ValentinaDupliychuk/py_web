from django_filters import rest_framework as filters
from django.db.models import QuerySet

from blog_ToDoList.models import Note
from . import serializers


class FilterNote(filters.FilterSet):
    class Meta:
        model = Note
        fields = ['significance',
                'public',
                'rating']


def AuthFilter(queryset:QuerySet, author_id:[int]):
    if author_id:
        return queryset.filter(author_id=author_id)
    else:
        return queryset


def public_filter(qeryset:QuerySet, public):
    return qeryset.filter(public=public)
