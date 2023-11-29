from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('contactUs', views.ContactUs, name='contactUs'),
    path('event', views.EventPage, name='event'),
    path('alumni', views.AlumniPage, name='alumni'),
    path('joiningform', views.JoiningForm, name='joiningform'),
]
