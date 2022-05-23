from django.urls import path
from common import views

urlpatterns = [
    path('hello/', views.Hello_World.as_view()),
    path("", views.IndexView.as_view()),
    ]