from django.db import models

from .category import Category
from .promotion import Promotion

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True)
    url_img = models.CharField(max_length=100, blank=True)
    category_id = models.ManyToManyField(Category, related_name='product_id')
    promotion_id = models.ManyToManyField(Promotion, related_name='product_id', blank=True)

    def __str__(self):
        return f"{self.name}, {self.price}, {self.description}"