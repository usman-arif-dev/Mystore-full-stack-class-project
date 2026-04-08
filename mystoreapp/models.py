from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.CharField(max_length=90)
    is_seller = models.BooleanField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profilepics/')
    
    def __str__(self):
        return self.username
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    stk_available = models.IntegerField()
    picture = models.ImageField(upload_to='products_images')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='product_owner')
    
    def __str__(self):
        return self.name
    
class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Product_cart')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cartitems_owner')
    quantity = models.IntegerField()
    
class Cart(models.Model):
    cartitem = models.ForeignKey(CartItems, on_delete=models.CASCADE, related_name='cartparent')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cart_owner')
    price = models.IntegerField()

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='Product_order')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orderitem_owner')
    quantity = models.IntegerField()
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_product')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order_owner')
    price = models.IntegerField()
    address = models.TextField()
    phone_no = models.CharField(max_length=15)
    
    
    