from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from users.forms import SignUpForm, SignInForm

def sign_up(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('sign_in')
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

def sign_in(request):
    if request.method =='POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('article_func')
    form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})
# Create your views here.

def sign_out(request):
    logout(request)
    return redirect('sign_in')
