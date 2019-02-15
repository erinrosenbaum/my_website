from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'weather'

urlpatterns = [
    path('', views.index, name='weather_list'),
    path('detail/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('delete/<int:pk>/', views.CityDeleteView.as_view(), name='city_delete'),
    path('new/', views.CityCreateView.as_view(), name='new_city'),
]
