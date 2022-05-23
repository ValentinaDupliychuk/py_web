from django.urls import path
from test_app import views

urlpatterns = [
    path('datetime/', views.DateTimeView.as_view()),
    path('random_number/', views.RandomNumber.as_view())
]
