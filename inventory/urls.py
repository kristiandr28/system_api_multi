from django.urls import path
from .views import CategoryList, CategoryDetail, ProductList, ProductDetail, SizeList, SizeDetail, ProductSizeDetail, ProductSizeList, OrderList, OrderDetail, OrderItemList, OrderItemDetail

urlpatterns = [
    path('api1/inventory/category/', CategoryList.as_view(), name='category-list'),
    path('api1/inventory/category/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('api1/inventory/product/', ProductList.as_view(), name='product-list'),
    path('api1/inventory/product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('api1/inventory/size/', SizeList.as_view(), name='size-list'),
    path('api1/inventory/size/<int:pk>/', SizeDetail.as_view(), name='size-detail'),
    path('api1/inventory/productsize/', ProductSizeList.as_view(), name='productsize-list'),
    path('api1/inventory/productsize/<int:pk>/', ProductSizeDetail.as_view(), name='productsize-detail'),
    path('api1/inventory/order/', OrderList.as_view(), name='order-list'),
    path('api1/inventory/order/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
    path('api1/inventory/orderitem/', OrderItemList.as_view(), name='orderitem-list'),
    path('api1/inventory/orderitem/<int:pk>/', OrderItemDetail.as_view(), name='orderitem-detail'),
]