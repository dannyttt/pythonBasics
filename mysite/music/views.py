from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

app_name = "music"
# Create your views here.
def home(request):
    # render(request, "music/home.html")
    return HttpResponse("this is the music page")
