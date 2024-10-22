from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Category, Product
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


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
