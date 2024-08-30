from django.db import models

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models. TextField()
    phone_number = models.IntegerField()
    
    def __str__(self):
        return self.name
        