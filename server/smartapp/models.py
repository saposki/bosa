from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class About(models.Model):
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='upload_location',
            null=True, blank=True,
            width_field='width_field',
            height_field='height_field')

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload_location',
            null=True, blank=True,
            width_field='width_field',
            height_field='height_field')
    description = models.CharField(max_length=1000)
    link = models.URLField(max_length=500)
    github = models.URLField(max_length=500)

class Musings(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='upload_location',
            null=True, blank=True,
            width_field='width_field',
            height_field='height_field')
    description = models.CharField(max_length=1000)
