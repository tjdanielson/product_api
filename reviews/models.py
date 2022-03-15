from django.db import models
from products.models import Product

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    stars = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)