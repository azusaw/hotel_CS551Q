from django.urls import path,include
import django.contrib.auth.urls
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('all', views.disaster_list, name='all'),
    path('detail/<slug:disasterNo>/', views.disaster_detail, name='detail'),
    path('search', views.search, name='search'),
    path('new', views.disaster_new, name='disaster_new'),
    path('edit/<slug:disasterNo>', views.disaster_edit, name='disaster_edit'),
    path('delete/<slug:disasterNo>', views.disaster_delete, name='disaster_delete'),
    path('chart/', views.chart, name='chart'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),


]