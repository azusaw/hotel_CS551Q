from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all', views.disaster_list, name='all'),
    path('detail/<slug:disasterNo>/', views.disaster_detail, name='detail'),
    path('search', views.search, name='search'),
    path('comparison', views.comparison, name='comparison'),
    path('new', views.disaster_new, name='disaster_new'),
    path('edit/<slug:disasterNo>', views.disaster_edit, name='disaster_edit'),
    path('delete/<slug:disasterNo>', views.disaster_delete, name='disaster_delete'),
    path('chart/', views.chart, name='chart'),

]
