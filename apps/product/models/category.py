from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    img = models.ImageField('img', upload_to='category/', max_length=250, blank=True)

    def __str__(self):
        return f"{self.name}, {self.description}"
    