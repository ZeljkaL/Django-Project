from django.urls import path
from django.conf.urls import include, url
from . import views
from django.contrib import admin
app_name = 'users'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('errorpage/', views.errorpage, name='errorpage'),
    path("accounts/", include("django.contrib.auth.urls"), name='accounts'),
    path("register/", views.register, name="register"),

]
