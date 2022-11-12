from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('products/', views.all_products, name='all_products'),
    path('<product_id>', views.view_product, name='view_product'),
]