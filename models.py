from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    intro = models.CharField(max_length=500)
    text = models.TextField()
    created = models.DateTimeField(auto_created=True)
    owner = models.OneToOneField(User)
    category = models.OneToOneField(Category)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'