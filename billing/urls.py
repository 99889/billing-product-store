from django.urls import path
from .views import ProductListCreate, ProductRetrieveUpdateDestroy, CustomerListCreate, CustomerRetrieveUpdateDestroy, SaleListCreate, SaleRetrieveUpdateDestroy
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-retrieve-update-destroy'),
    path('sales/', SaleListCreate.as_view(), name='sale-list-create'),
    path('sales/<int:pk>/', SaleRetrieveUpdateDestroy.as_view(), name='sale-retrieve-update-destroy'),
    path('login/', views.employee_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-product/', views.add_product, name='add-product'),
    path('product-management/', views.product_management, name='product_management'),
]
