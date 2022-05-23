from django.shortcuts import render
from datetime import datetime
from random import random

from django.views import View
from django.http import HttpRequest, HttpResponse

class DateTimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)


class RandomNumber(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        random_number = random()

        return HttpResponse(random_number)