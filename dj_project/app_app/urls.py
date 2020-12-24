from django.urls import path,include
from app_app import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index),
    path('app/',views.sec),
    path('sec',views.new)

]
