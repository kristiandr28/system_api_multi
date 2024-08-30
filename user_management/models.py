from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    signup_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username