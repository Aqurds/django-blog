from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ecommerce-home'),
    path('about/', views.about, name='ecommerce-about'),
    path('contact/', views.contact, name='ecommerce-contact')
]
