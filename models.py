from django.db import models
from django.contrib.auth.models import User # This is the built-in User system

class Category(models.Model):
    name = models.CharField(max_length=100)
    # This magic line connects the board to whoever created it!
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.name

class Craft(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='crafts/')
    # This keeps the original 'global' category for the main feed
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
