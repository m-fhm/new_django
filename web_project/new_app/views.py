from django.shortcuts import render
from new_app.forms import colform
from new_app.models import school

# Create your views here.
def index(request):
    if request.method=="POST":
        form =colform(request.POST)
        if form.is_valid():
            form.save()
    form = colform()
    return render(request,"index.html",{'fm':form})
def view(request):
    data = school.objects.all()
    return render(request,"view.html",{'data':data})
def edit(request,id):
    fetch_data= school.objects.get(id=id)
    form = colform(instance=fetch_data)
    return render(request,'index.html',{'fm':form})