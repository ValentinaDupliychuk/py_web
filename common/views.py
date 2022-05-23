from django.shortcuts import render

from django.views import View
from django.http import HttpRequest, HttpResponse


class Hello_World(View):
    def get(self, request):
        note = f"Hello world!"
        return HttpResponse(note)


class IndexView(View):
    def get(self, request):
        return render(request, "common/index.html")
