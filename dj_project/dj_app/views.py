from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(abc):
    context={}
    context['name']="this is our trila "
    return render(abc,'index.html',context)
def new(abc):
    return HttpResponse("<h1> this for new of dj_app</h1>")
