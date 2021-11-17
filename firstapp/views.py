from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.core.mail import send_mail
from django.contrib import messages


def signupview(request):
    form = SignUpForm() #blank
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {username}!')
            send_mail(
                'Regarding New Account Creation',
                'Your Account has created succesfully',
                'swapnilpophale300@gamil.com',
                [user_email],
                fail_silently=False
            )
            return redirect('login')
    return render(request, 'signup.html', {'form':form})


def loginview(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request, 'login.html')

def loginsuccess(request):
    return render(request, 'loginsuccess.html')

def logoutview(request):
    logout(request)
    return redirect('login')
