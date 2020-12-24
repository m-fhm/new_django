# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(abc):
    return HttpResponse("<h1> this is  index of dj_app</h1>")
def new(abc):
    return HttpResponse("<h1> this for new of dj_app</h1>")
