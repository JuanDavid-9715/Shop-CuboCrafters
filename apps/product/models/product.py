from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True)
    url_img = models.CharField(max_length=100)
    category_name = models.ManyToManyField("Category", related_name='products')
    promotion_name = models.ManyToManyField("Promotion", related_name='products')

    def __str__(self):
        return f"{self.name}, {self.price}, {self.description}"