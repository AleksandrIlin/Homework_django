from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('create_blog/', BlogCreateView.as_view(), name='create_blog'),
    path('home/', BlogListView.as_view(), name='home'),
    path('home/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('home/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('home/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete')
]
