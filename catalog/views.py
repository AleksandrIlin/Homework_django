from urllib import request

from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from catalog.models import Category, Product


class CatalogCategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'category_list'


def product_list(request, category_name):
    products = Product.objects.filter(category__name=category_name)
    return render(request, 'catalog/product_list.html', {'object_list': products})


class CatalogProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'


class CatalogProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


class CatalogContactsView(View):
    @staticmethod
    def get(request):
        return render(request, 'catalog/contacts.html')

    @staticmethod
    def post(request):
        name = request.POST.get('name')
        massage = request.POST.get('massage')
        return HttpResponse(f"Спасибо, {name}. Сообщение получено.")
