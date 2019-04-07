from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add),
    path('create', views.create),
    path('find', views.find),
    path('date', views.date)
]