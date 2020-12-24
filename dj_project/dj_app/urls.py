from django.urls import path,include
from dj_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
       path('', views.index, name='new'),
       path('new', views.new, name='new'),
]
