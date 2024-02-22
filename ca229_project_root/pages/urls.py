from django.urls import path
from . import views

urlpatterns = [
    path('magic', views.magic, name = 'magic'),
    path('signup', views.signup, name = 'signup'),
    path('login', views.login, name = 'login'),
    path('about', views.about, name = 'about'),
    path('', views.index, name='index'),
]