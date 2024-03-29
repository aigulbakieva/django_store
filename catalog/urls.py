from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, category_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),
    path('category_list/', category_list, name='category_list'),
]
