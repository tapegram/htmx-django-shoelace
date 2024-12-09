from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "home.html")


def load_content(request):
    return HttpResponse("<p>This content was loaded with HTMX!</p>")
