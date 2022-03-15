from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory_quantity = models.IntegerField()
    image = models.URLField(default="https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930")