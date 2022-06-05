from rest_framework import serializers
from datetime import datetime

from blog_ToDoList.models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Note
        fields = "__all__"


class QueryParamsNotesFilterSignSerializer(serializers.Serializer):
    importance = serializers.ListField(child=serializers.BooleanField(),
                                       required=False)


class QueryParamsNotesFilterPublicSerializer(serializers.Serializer):
    is_public = serializers.ListField(child=serializers.BooleanField(),
                                      required=False)


class QueryParamsNotesFilterStatusSerializer(serializers.Serializer):
    status = serializers.ListField(child=serializers.IntegerField(),
                                   required=False)