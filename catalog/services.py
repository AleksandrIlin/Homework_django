from catalog.models import Product
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_products_from_cache():
    """Получает данные из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


def get_products_by_category(category_name):
    """Получает продукты по имени категории из кэша или базы данных."""
    key = f'products_by_category_{category_name}'
    products = cache.get(key)

    if products is not None:
        return products

    products = list(Product.objects.filter(category__name=category_name))
    cache.set(key, products)

    return products