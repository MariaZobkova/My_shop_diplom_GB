
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Теремок - Главная',
        'content': 'Магазин деревянных игрушек Теремок'
    }
    return render(request, 'mainapp/index.html', context)


def about(request):
    context = {
        'title': 'Теремок - О нас',
        'content': 'Самый лучший магазин игрушек!',
        'text': "Мы заботимся о вас и ваших детях"
    }
    return render(request, 'mainapp/about.html', context)

def info(request):
    context = {
        'title': 'Теремок - Контакты',
        'content': 'Контакты',
        'text1': 'Наш адрес: г. Петрозаводск, пр. Ленина, 105',
        'text2': 'Телефон: 88142 77 77 77',

    }
    return render(request, 'mainapp/info.html', context)
