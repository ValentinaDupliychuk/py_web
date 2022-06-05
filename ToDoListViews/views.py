from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters

from django.shortcuts import get_object_or_404

from blog_ToDoList.models import Note
from . import serializers, permissions, filters


class NoteListAPIView(APIView):
    """вывод всех "разрешенных" объектов"""
    permission_classes = (IsAuthenticated, permissions.EditPublicNotePermission)
    filter_backends = [DjangoFilterBackend]
    filtertodo = filters.FilterNote

    def get(self, request: Request) -> Response:
        notes = Note.objects.all()
        serializer = serializers.NoteSerializer(instance=notes, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        data = request.data
        note = Note(**data)
        note.save(force_insert=True)
        return Response(serializers.NoteSerializer(data), status=status.HTTP_201_CREATED)


class NoteDetailedAPIView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request: Request, pk) -> Response:
        queryset = get_object_or_404(Note, pk=pk)
        serializer_ = serializers.NoteSerializer(instance=queryset)
        if queryset.author != request.user:
            if queryset.public != 1:
                return Response(status.HTTP_404_NOT_FOUND)
        return Response(serializer_.data)

    def put(self, request: Request, pk) -> Response:
        note = Note.objects.get(pk=pk)
        if self.request.user != note.author:
            return Response('У Вас нет прав просмотра')

        serializer = serializers.NoteSerializer(
            instance=note, data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("Неверные данные", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk) -> Response:
        queryset = get_object_or_404(Note, pk=pk)
        serializer = serializers.NoteSerializer(instance=queryset, data=request.data)
        if queryset.author != request.user:
            return Response('У Вас нет прав просмотра')

        if serializer.is_valid():
            serializer.save(author=request.user)
            queryset.delete()
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)


class NoteListAuthorAPIView(generics.ListCreateAPIView):
    """
    Выводит записи только автора
    """
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = (IsAuthenticated, permissions.EditNotePermission)

    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.FilterNote

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user).order_by('-public', '-significance')

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class PublicNotesAPIView(generics.ListAPIView):

    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer
    permission_classes = (IsAuthenticated, permissions.EditPublicNotePermission)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(public=True).order_by('-public', '-significance')


