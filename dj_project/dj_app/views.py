from django.shortcuts import render
from django.http import HttpResponse
from dj_app import forms

# Create your views here.
def index(abc):
    context={}
    context['name']="this is our trila "
    return render(abc,'index.html',context)
def new(abc):
    return HttpResponse("<h1> this for new of dj_app</h1>")
def page(request):
    form=forms.myform()
    if request.method=='POST':
        form = forms.myform(request.POST)
        if form.is_valid():
            print("Name:"+form.cleaned_data['name'])
            print("email:"+form.cleaned_data['email'])

    return render(request,'form.html',{'form':form})
