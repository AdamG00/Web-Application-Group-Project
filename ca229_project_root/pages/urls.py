from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('<int:num1>/<str:op>/<int:num2>/<str:op2>/<int:num3>/', views.magic_page, name ='magic_page'),
    path('admin/', views.index, name='admin'),
    path('magic/', views.magic, name='magic'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]
