from django.http import HttpResponse
from django.views.generic import View,TemplateView,ListView
from .models import school

class MyView(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')

class template_view(TemplateView):
    template_name = 'new.html'
    def get_context_data(self,**kwargs):

        context=super().get_context_data(**kwargs)
        context['key1'] = "this is the valued key"
        return context
class school_view(ListView):
    context_object_name = 'sch'
    model = school










# from django.shortcuts import render, redirect
# from new_app.forms import colform
# from new_app.models import school

# # Create your views here.
# def index(request):
#     if request.method=="POST":
#         form =colform(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('view') 
#     else:    
#         form = colform()
#         return render(request,"form.html",{'fm':form})
# def view(request):
#     data = school.objects.all()
#     return render(request,"view.html",{'data':data})
# def edit(request,id):
#     if request.method == "POST":
#         fetch_data= school.objects.get(id=id)
#         form = colform(request.POST, instance= fetch_data)
#         if form.is_valid():
#             form.save()
#         return redirect('view')
#     else:
#         fetch_data= school.objects.get(id=id)
#         form = colform(instance=fetch_data)
#         return render(request,'form.html',{'fm':form})
# def delete(request, id):
#     fetch_data= school.objects.get(id=id)
#     fetch_data.delete()
#     return redirect('view')