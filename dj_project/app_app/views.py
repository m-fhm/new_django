from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(resp):
    return HttpResponse("this is the index of app_app")
def new(resp):
    return HttpResponse("this is the index of app_app")
def sec(dfa):
    return HttpResponse("this is the view for app_app second")