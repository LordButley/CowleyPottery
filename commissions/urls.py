from django.urls import path
from . import views

urlpatterns = [
    path('', views.commissions_form_view, name='commissions'),
    path('success/', views.commissions_success, name='commissions_success'),
]