from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, category_list, product_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', category_list, name='category_list'),
    path('contacts/', contacts, name='contacts'),
    path('product_list/', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail')

]
