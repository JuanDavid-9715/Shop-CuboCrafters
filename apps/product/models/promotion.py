from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage

from PIL import Image
import uuid
import os

def img_path(instance, filename):
    random_filename = str(uuid.uuid4())
    extension = os.path.splitext(filename)[1]

    return 'promotion/{}{}'.format(random_filename, extension)

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.IntegerField()
    description = models.TextField(blank=True)
    img = models.ImageField(
        default='default/errorPromotion.webp',
        upload_to=img_path 
    )
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.pk and self.img.name != 'default/errorPromotion.webp':
            old_promotion = Promotion.objects.get(pk=self.pk)
            default_img_path = os.path.join(settings.MEDIA_ROOT, 'default/errorPromotion.webp')

            if old_promotion.img.path != self.img.path and old_promotion.img.path != default_img_path:
                default_storage.delete(old_promotion.img.path)

        super(Promotion, self).save(*args, **kwargs)

        if self.img and os.path.exists(self.img.path):
            with Image.open(self.img.path) as img:
                width, height = img.size

                if width > height:
                    new_height = 500
                    new_width = int((width/height) * new_height)
                    img = img.resize((new_width, new_height))
                    img.save(self.img.path)
                elif height > width:
                    new_width = 500
                    new_height = int((height/width) * new_width )
                    img = img.resize((new_width, new_height))
                    img.save(self.img.path)
                else:
                    img.thumbnail((500, 500))
                    img.save(self.img.path)

    def __str__(self):
        return f"{self.name}, {self.price}, {self.discount}, {self.description}"