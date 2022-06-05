from django.shortcuts import render

from django.views import View
from django.http import HttpRequest, HttpResponse


class Hello_World(View):
    def get(self, request):
        note = f"Hello world!"
        return HttpResponse(note)


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"user": request.user.username, "version": "3.6"}
        return render(request, "common/index.html", context)

