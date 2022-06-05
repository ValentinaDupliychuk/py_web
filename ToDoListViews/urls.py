from django.urls import path
from . import views

urlpatterns = [
    path('notes_all/', views.NoteListAPIView.as_view()),
    path('note/<int:pk>', views.NoteDetailedAPIView.as_view()),
    path('public/', views.PublicNotesAPIView.as_view()),
    path('filterauthor/', views.NoteListAuthorAPIView.as_view()),

]
