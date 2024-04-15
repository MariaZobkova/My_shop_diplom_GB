from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'home',
        'content': 'Главная страница'
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    return HttpResponse("About page")
