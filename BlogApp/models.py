from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
status_choice= (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('categories', args=[str(self.slug)])

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name='Tag')
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags', args=[str(self.slug)])


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug =models.SlugField(unique=True)
    feature_image = models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Picture')
    content = RichTextUploadingField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name="Category")
    status = models.CharField(choices=status_choice, default='draft', max_length=10)
    published_date = models.DateTimeField(verbose_name="Created on")
    author = models.CharField(default='Anonymous', max_length=50, verbose_name='Created by')
    tag = models.ManyToManyField(Tag, verbose_name='Tag')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('postdetails', args=[str(self.slug)])

class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name= 'Name')
    email = models.EmailField()
    msg = models.TextField()
    msg_date = models.DateTimeField()

    def __str__(self):
        return self.name
