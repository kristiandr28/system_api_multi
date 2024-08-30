from django.contrib import admin
from .models import Category, Product, Size, ProductSize, StockMovement, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'sku', 'color', 'created_at', 'updated_at']
    search_fields = ['name', 'sku']
    list_filter = ['category']

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ['size', 'description']

@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'stock']
    list_filter = ['product']

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'quantity', 'movement_type', 'created_at']
    list_filter = ['movement_type', 'product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email', 'date', 'status']
    search_fields = ['customer_name', 'customer_email']
    list_filter = ['status']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'size', 'quantity', 'price']
    list_filter = ['order', 'product']

