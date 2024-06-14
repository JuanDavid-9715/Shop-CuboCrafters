from django.db import models

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.IntegerField()
    description = models.TextField(blank=True)
    url_img = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}, {self.price}, {self.discount}, {self.description}"