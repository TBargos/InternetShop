from django import template # для регистрации шаблонного тега через применение декоратора
from django.utils.http import urlencode # лучше не путать, есть и другие модули с urlencode


from goods.models import Categories # для работы с таблицей Категории в БД через запросы в Django


register = template.Library()


@register.simple_tag()
def tag_categories():
    """Загружает список категорий как объекты из БД. Был написан и применён в base.html"""
    return Categories.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs): # context попадает в html шаблон из контроллера
    query = context['request'].GET.dict() # запрашивает из запроса параметры в формате словаря
    query.update(kwargs) # запихивает в словарь переданные именованные аргументы
    return urlencode(query) # возвращает ключи и значения в формате для браузера