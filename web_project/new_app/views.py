from django.shortcuts import render, redirect
from new_app.forms import colform
from new_app.models import school

# Create your views here.
def index(request):
    if request.method=="POST":
        form =colform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('view') 
    else:    
        form = colform()
        return render(request,"form.html",{'fm':form})
def view(request):
    data = school.objects.all()
    return render(request,"view.html",{'data':data})
def edit(request,id):
    if request.method == "POST":
        fetch_data= school.objects.get(id=id)
        form = colform(request.POST, instance= fetch_data)
        if form.is_valid():
            form.save()
        return redirect('view')
    else:
        fetch_data= school.objects.get(id=id)
        form = colform(instance=fetch_data)
        return render(request,'form.html',{'fm':form})
def delete(request, id):
    fetch_data= school.objects.get(id=id)
    fetch_data.delete()
    return redirect('view')