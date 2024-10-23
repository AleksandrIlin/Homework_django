from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Category, Product
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from catalog.services import get_products_by_category, get_products_from_cache


class CatalogCategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'category_list'


class CatalogProductByCategoryView(View):
    model = Category

    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        products = get_products_by_category(category_name)

        return render(request, 'catalog/category_products.html',
                      {'category': category, 'products': products})


class CatalogProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return get_products_from_cache()


class CatalogProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:category_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class CatalogProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:category_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_unpublish_product'):
            return ProductModeratorForm
        raise PermissionDenied


class CatalogProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy('catalog:category_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.has_perm('catalog.delete_product')

    def handle_no_permission(self):

        return redirect('catalog:category_list')


class CatalogProductDetailView(LoginRequiredMixin, DetailView):
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
