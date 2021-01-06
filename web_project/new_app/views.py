from django.shortcuts import render
from new_app.forms import colform
from new_app.models import school

# Create your views here.
def index(request):
    data = school.objects.all()
    return render(request,"index.html",{'data':data})

    if request.method=="POST":
        form =colform(request.POST)
        if form.is_valid():
            form.save()
    form = colform()
    return render(request,"index.html",{'fm':form})
