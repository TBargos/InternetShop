from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products


def catalog(request, category_slug: str):
    """Показывает товары выбранной категории или все"""
    page = int(request.GET.get('page', 1))
    
    if category_slug == 'all':  # все товары
        goods = Products.objects.all()
    else:
        # Возвращает QuerySet из товаров или выбрасывает ошибку 404, если QuerySet пуст
        goods: list[Products] = get_list_or_404(\
            Products.objects.filter(category__slug=category_slug))
    
    paginator = Paginator(goods, 3)
    current_page = paginator.page(page)
    
    context = {
        "title": "Home - Каталог",
        "goods": current_page,
        "slug_url": category_slug
    }
    return render(request, "goods/catalog.html", context)


def product(request, product_slug: str):
    """Загружает страницу выбранного товара"""
    product: Products = Products.objects.get(slug=product_slug)
    
    context: dict[str, Products] = {
        "product": product
    }
    
    return render(request, "goods/product.html", context=context)
 