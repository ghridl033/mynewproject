from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup', views.signup),
    path('login', views.login),
    path('login2', views.login2),
    path('members', views.login_after),
    path('logout', views.logout)
]
