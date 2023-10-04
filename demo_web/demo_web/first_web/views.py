from django.shortcuts import render
from django.http import HttpResponse, request


# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about_us.html")

def registration(request):
    return render(request, "registration.html")
