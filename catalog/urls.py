from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import CatalogContactsView, CatalogCategoryListView, CatalogProductListView, \
    CatalogProductDetailView, CatalogProductCreateView, CatalogProductUpdateView, CatalogProductDeleteView

app_name = CatalogConfig.name


urlpatterns = [
    path('', CatalogCategoryListView.as_view(), name='category_list'),
    path('contacts/', CatalogContactsView.as_view(), name='contacts'),
    path('category/<str:category_name>/', views.product_list, name='product_list'),
    path('product/<int:pk>/', CatalogProductDetailView.as_view(), name='product_detail'),
    path('product_list/', CatalogProductListView.as_view(), name='product_list'),
    path('product/create/', CatalogProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', CatalogProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', CatalogProductDeleteView.as_view(), name='product_delete')

]
