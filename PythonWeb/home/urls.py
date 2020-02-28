from django.urls import path
from django.contrib import admin 
from . import views
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('', views.index),
    path('contact/', views.contact, name = 'contact'),
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.login, {'template_name':'pages/login.html'}, name='login' )
]