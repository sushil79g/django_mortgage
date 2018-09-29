from single import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('mail/', views.mail, name='mail'),
]
