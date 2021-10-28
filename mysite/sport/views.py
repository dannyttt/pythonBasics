from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

app_name = "sport"


def home(request):
    return HttpResponse("this is the sport home page")
