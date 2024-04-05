from django.http import HttpResponse
from django.shortcuts import render # отрисовывает html страницу для отправки пользователю

def index(request):    # Контроллер главной страницы, request содержит информацию о запросе
    context = {
        'title': 'Home',
        'content': 'Главная страница - HOME'
    }

    return render(request, 'main/index.html', context)

def about(request):    # Контроллер главной страницы, request содержит информацию о запросе
    return HttpResponse("About page")   # Возвращает какой-либо ответ