from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
 