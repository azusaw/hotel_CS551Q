from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all', views.disaster_list, name='all'),
    path('detail/<slug:disasterNo>/', views.disaster_detail, name='detail'),
    path('search', views.search, name='search'),
    path('comparison', views.comparison, name='comparison'),
]
