from django.db import models
from io import BytesIO
from django.core.files import File
from PIL import Image
import cloudinary
from cloudinary.models import CloudinaryField

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

   