from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('products/', views.all_products, name='all_products'),
]