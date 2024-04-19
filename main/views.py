from django.http import HttpResponse
from django.shortcuts import render # для отрисовки html страницы для отправки пользователю

def index(request):    # Контроллер главной страницы, request содержит информацию о запросе
    context = {
        'title': "Home - главная",
        'content': "Магазин мебели HOME"
    }
    return render(request, 'main/index.html', context)

def about(request):    # Контроллер about-страницы, request содержит информацию о запросе
    context = {
        'title': "О нас",
        'content': "Home - О нас",
        'text_on_page': "Мы такие классные, что даже страшно, и вот 100500 причин:"
    }
    return render(request, 'main/about.html', context)