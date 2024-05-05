from django.http import HttpResponse
from django.shortcuts import render # для отрисовки html страницы для отправки пользователю

from goods.models import Categories # для работы с таблицей Категории в БД через запросы в Django


def index(request):    # Контроллер главной страницы, request содержит информацию о запросе
    categories = Categories.objects.all()
    
    context = {
        'title': "Home - главная",
        'content': "Магазин мебели HOME",
        'categories': categories
    }
    return render(request, 'main/index.html', context)

def about(request):    # Контроллер about-страницы, request содержит информацию о запросе    
    context = {
        'title': "О нас",
        'content': "Home - О нас",
        'text_on_page': "Мы такие классные, что даже страшно, и вот 100500 причин:",
    }
    return render(request, 'main/about.html', context)