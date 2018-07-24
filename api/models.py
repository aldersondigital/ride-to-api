from __future__ import unicode_literals
from django.db import models

class Category(models.Model):
    """This class represents the Product model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=255, blank=False, unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class Product(models.Model):
    """This class represents the Product model."""
    category = models.ForeignKey(Category, null=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    description = models.CharField(max_length=255, blank=False, unique=False)
    link = models.CharField(max_length=255, blank=False, unique=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
