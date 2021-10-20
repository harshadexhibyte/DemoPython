from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Dashboard', views.Dashboard, name='Dashboard'),
    path('fileUploded',views.fileUploded,name='fileUploded'),
]
