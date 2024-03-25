# ecom/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)

class Recommendation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserClick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    clicked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} clicked on {self.product.name} at {self.clicked_at}"