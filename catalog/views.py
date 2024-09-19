from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from catalog.models import Category, Product


# def home(request):
#     return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        massage = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}. Сообщение получено.")
    return render(request, 'contacts.html')


def category_list(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, 'category_list.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, 'product_detail.html', context)

