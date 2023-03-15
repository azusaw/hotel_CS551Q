from django.urls import path

from . import views

urlpatterns = [
    path('', views.disaster_list, name='home'),
    path('all', views.disaster_list, name='all'),
    path('search', views.disaster_search, name='search'),
]
