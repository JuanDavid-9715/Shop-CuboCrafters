from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url_img = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}, {self.description}"
    