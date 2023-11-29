from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from MUPC import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from authentication import views
from authentication import models
from django.contrib import messages


def ContactUs(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('text')
        send_mail(subject,message, email,[settings.EMAIL_HOST_USER])
    return render(request, "ContactUs.html")


def EventPage(request):
    return render(request, "EventPage.html")

def AlumniPage(request):
    return render(request, "AlumniPage.html")


def JoiningForm(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
    return render(request, "JoiningForm.html")