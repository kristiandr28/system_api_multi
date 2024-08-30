import datetime
import random
from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    COLOR_CHOICE = [
        ('merah', 'Merah'),
        ('hitam', 'Hitam'),
        ('kuning', 'Kuning'),
        ('hijau', 'Hijau'),
        ('biru', 'Biru'),
        ('putih', 'Putih'),
        ('ungu', 'Ungu'),
        ('coklat', 'Coklat'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=20, unique=True, blank=True)
    color = models.CharField(max_length=10, choices=COLOR_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.sku:
            self.sku = self.generate_sku()
        super(Product, self).save(*args, **kwargs)

    def generate_sku(self):
        category_prefix = self.category.name[:3].upper()
        unique_number = str(random.randint(1000, 9999))
        date_part = datetime.datetime.now().strftime('%d%m%y')
        
        return f"{category_prefix}{unique_number}{date_part}"

    def __str__(self):
        return self.name
    
class Size(models.Model):
    size = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.size

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sizes')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='product_sizes')
    stock = models.IntegerField()
    
    def __str__(self):
        return f"{self.product.name} - {self.size.size} ({self.stock})"
    
class StockMovement(models.Model):
    MOVEMENT_TYPES = [
        ('addition', 'Addition'),
        ('subtraction', 'Subtraction')
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stock_movements')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='stock_movements')
    quantity = models.IntegerField()
    movement_type = models.CharField(max_length=11, choices=MOVEMENT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.movement_type} ({self.quantity})"
    
class Order(models.Model):
    STATUS_ORDER = [
        ('pending', 'Pending'),
        ('processed', 'Prosessed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ]
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=11, choices=STATUS_ORDER)
    
    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} ({self.size.size}) - Quantity: {self.quantity}"
