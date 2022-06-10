from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
from sortedm2m.fields import SortedManyToManyField

# Create your models here
class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=255)
	article = SortedManyToManyField('Article', blank=True)

	def __str__(self):
		return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField()
    alamat = models.CharField(max_length=255)
    telepon = models.CharField(max_length=12)
    jam = models.CharField(max_length=15)
    harga = models.TextField()
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="destinasi")
    Category = SortedManyToManyField(Category, related_name="category")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Oleholeh(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    content = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to="oleholeh")
    
    def __str__(self):
        return self.title

class Kuliner(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    content = RichTextField()
    image = models.ImageField(null=True, blank=True, upload_to="kuliner")
    
    def __str__(self):
        return self.title