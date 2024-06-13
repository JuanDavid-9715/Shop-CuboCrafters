from django.db import models

class Promotions(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    price = models.FloatField()
    discount = models.IntegerField()
    description = models.TextField(blank=True)
    url_img = models.CharField(max_length=100, blank=True)