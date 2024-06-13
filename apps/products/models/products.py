from django.db import models

class Products(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    price = models.FloatField()
    description = models.TextField(blank=True)
    url_img = models.CharField(max_length=100)
    categories_name = models.ManyToManyField("Categories", related_name='products')
    promotions_name = models.ManyToManyField("Promotions", related_name='products')