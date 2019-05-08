from django.urls import path

from . import views

app_name = 'stock_market'

urlpatterns = [
    path('', views.index, name='stock_list'),
    path('detail/<int:pk>/', views.StockDetailView.as_view(), name='stock_detail'),
    path('delete/<int:pk>/', views.StockDeleteView.as_view(), name='stock_delete'),
    path('new/', views.StockCreateView.as_view(), name='new_stock'),
]
