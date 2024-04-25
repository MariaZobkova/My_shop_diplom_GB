from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .forms import ClientLoginForm, ClientRegistrationForm, ProfileForm
from django.urls import reverse
from .models import Client


def login(request):
    if request.method == 'POST':
        form = ClientLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            client = authenticate(username=username, password=password)
            if client is not None:
                auth.login(request, client)
                return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = ClientLoginForm()
    context = {
        'title': 'Теремок - Авторизация',
        'form': form
    }
    return render(request, 'clients/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            client = form.instance
            auth.login(request, client)
            return HttpResponseRedirect(reverse('mainapp:index'))
    else:
        form = ClientRegistrationForm()
    context = {
        'title': 'Теремок - Регистрация',
        'form': form
    }
    return render(request, 'clients/registration.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('client:profile'))
    else:
        form = ProfileForm(instance=request.user)
    context = {
        'title': 'Теремок - Кабинет',
        'form': form,
    }
    return render(request, 'clients/profile.html', context=context)


@login_required
def logout(request):
    # auth.logout(request)
    return redirect(reverse('mainapp:about'))
