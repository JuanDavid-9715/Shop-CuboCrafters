from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage

from PIL import Image
import uuid
import os

def img_path(instance, filename):
    random_filename = str(uuid.uuid4())
    extension = os.path.splitext(filename)[1]

    return 'category/{}{}'.format(random_filename, extension)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    img = models.ImageField(
        default='default/errorCategory.webp',
        upload_to=img_path 
    )

    def save(self, *args, **kwargs):
        if self.pk and self.img.name != 'default/errorCategory.webp':
            old_category = Category.objects.get(pk=self.pk)
            default_img_path = os.path.join(settings.MEDIA_ROOT, 'default/errorCategory.webp')

            if old_profile.img.path != self.img.path and old_profile.img.path != default_img_path:
                default_storage.delete(old_category.img.path)

        super(Category, self).save(*args, **kwargs)

        if self.img and os.path.exists(self.img.path):
            with Image.open(self.img.path) as img:
                width, height = img.size

                if width > height:
                    new_height = 300
                    new_width = int((width/height) * new_height)
                    img = img.resize((new_width, new_height))
                    img.save(self.img.path)
                elif height > width:
                    new_width = 300
                    new_height = int((height/width) * new_width )
                    img = img.resize((new_width, new_height))
                    img.save(self.img.path)
                else:
                    img.thumbnail((300, 300))
                    img.save(self.img.path)

            with Image.open(self.img.path) as img:
                width, height = img.size

                if width > height:
                    left = (width - height) / 2
                    top = 0
                    right = (width + height) / 2
                    bottom = height

                else:
                    left = 0
                    top = (height - width) / 2
                    right = width
                    bottom = (height + width) / 2

                img = img.crop((left, top, right, bottom))
                img.save(self.img.path)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}, {self.description}"
    