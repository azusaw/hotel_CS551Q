from django.urls import path
from . import views

urlpatterns = [
    path('', views.disaster_list, name='disaster_list'),
]