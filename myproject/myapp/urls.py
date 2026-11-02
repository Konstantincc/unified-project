from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('network/', views.network_monitor, name='network_monitor'),
]
