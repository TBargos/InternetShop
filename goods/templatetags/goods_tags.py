from django import template # для регистрации шаблонного тега через применение декоратора

from goods.models import Categories # для работы с таблицей Категории в БД через запросы в Django


register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()