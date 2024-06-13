from django.db import models

class Categories(models.Model):
    name = models.CharField(primary_key=True, max_length=100)
    description = models.TextField(blank=True)
    url_img = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}, {self.description}"
    