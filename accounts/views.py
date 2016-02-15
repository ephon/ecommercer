from django.shortcuts import HttpResponseRedirect, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from .forms import LoginForm, RegisterForm
from .models import MyUser
# Create your views here.

def auth_login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return render(request, 'login.html', locals())
        if next_url is not None:
            return HttpResponseRedirect(next_url)
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'login.html', locals())


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password2"]
        # MyUser.objects.create_user(username=username, email=email, password=password)
        new_user = MyUser()
        new_user.username = username
        new_user.email = email
        new_user.set_password(password)
        new_user.save()
        return redirect('login')
    else:
        return render(request, 'register.html', locals())



