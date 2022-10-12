from site import abs_paths
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.

def register(request):
    context = {
        'error_message': ''
    }
    valid = False
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if username == '' or email == '' or password1 == '' or password2 == '':
            valid = False
            context['error_message'] = 'Please ensure all fields are appropriately filled.'
        elif len(password1) < 5:
            valid = False
            context['error_message'] = 'Please ensure password is not less than 5 characters.'
        else:
            valid = True
        
        if valid == True:
            if password1 == password2:
                user = authenticate(username=username, email=email)
                if user is None:
                    new_user = User.objects.create_user(username=username, email=email, password=password1)
                    new_user.save()
                    login(request, new_user)
                    return redirect('dashboard')
                else:
                    context['error_message'] = "There is already a user associated with the following credentials. Would you like to login?"
            else:
                context['error_message'] = 'Please make sure both passwords match.'
    return render(request, 'authentication/register.html', context)

def logIn(request):
    context = {
        'error_message': ''
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            context['error_message'] = "Did you put in the right credentials? Try registering"
    return render(request, 'authentication/login.html', context)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_id = User.objects.get(email=email).id
        send_mail(
            'This is your password. Thanks for using my services', 
            request.build_absolute_uri(reverse('change_password', args=(user_id, ))), 
            'davidukemeekong1@gmail.com', 
            [email], 
            fail_silently=False)
    return render(request, 'authentication/forgot_password.html')

def change_password(request, pk):
    context = {
        'error_message': ''
    }
    if request.method == "POST":
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            user = User.objects.get(pk=pk)
            user.set_password(password1)
            user.save()
            return redirect('logIn')
        else:
            context['error_message'] = 'Please make sure both passwords match.'
    return render(request, 'authentication/change_password.html', context)

def dashboard(request):
    context = {
        'user': request.user
    }
    if request.method == 'POST':
        logout(request)
        return redirect('logIn')
    return render(request, 'authentication/dashboard.html', context)