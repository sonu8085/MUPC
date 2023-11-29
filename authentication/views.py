from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from MUPC import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from . tokens import generate_token

def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist!")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')
        my_user = User.objects.create_user(username, email, pass1)
        my_user.first_name = name
        my_user.is_active = False
        my_user.save()
        messages.success(request, "Your Account has been created succesfully!!")
        
        # Welcome Email
        subject = "Welcome to Medi-Caps University Placement Cell Login!!"
        message = "Hello \n" + my_user.first_name + "Welcome to MUPC!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nSonu Banjara"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [my_user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation email
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ MUPC - Django Login!!"
        message2 = render_to_string('email_confirmation.html', {
            'name' : my_user.first_name,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token' : generate_token.make_token(my_user)
        })

        email = EmailMessage(email_subject, message2, settings.EMAIL_HOST_USER, [my_user.email],)
        email.fail_silently=True
        email.send()


        return render(request, "signin.html")
    return render(request, "signup.html")
def activate(request, uidb64, token):
    try: 
        uid = force_str(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None
    
    if my_user is not None and generate_token.check_token(my_user, token):
        my_user.is_active = True
        my_user.save()
        login(request, my_user)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            messages.error(request, "Invalid Credentials!!")
            return render(request, "signin.html")
    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request,"You successfully Logged Out. ")
    return render(request, "signin.html")


