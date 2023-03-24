from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all', views.disaster_list, name='all'),
    path('detail/<slug:disasterNo>/', views.disaster_detail, name='detail'),
    path('search', views.search, name='search'),
    path('comparison', views.comparison, name='comparison'),
    path('disaster_new/', views.disaster_new, name='disaster_new'), #'bear_new/'是地址名，views.bear_new是views.py中定义的def的名字，最终返回的是views.py中def的render的模板
    path('disaster/<slug:disasterNo>/edit', views.disaster_edit, name='disaster_edit'),
    path('disaster/<slug:disasterNo>/delete',views.disaster_delete, name='disaster_delete'),
]
