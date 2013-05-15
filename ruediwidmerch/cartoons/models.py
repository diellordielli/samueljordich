# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Cartoon(models.Model):
    IMAGE_WIDTH = (
        ('1', '1'),
        ('2', '2'),
        ('4', '4'),
    )

    IMAGE_HEIGHT = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )

    description = models.TextField(blank=True)
    ordering = models.IntegerField(blank=True)
    category = models.CharField(max_length=200)
    date = models.DateTimeField()
    image = models.ImageField(upload_to="cartoons")
    width = models.CharField(max_length=20, choices=IMAGE_WIDTH)
    height = models.CharField(max_length=20, choices=IMAGE_HEIGHT)

    class Meta:
        verbose_name_plural = "Cartoons"

    def __unicode__(self):
        return u"%s %s" % (self.description,  self.category)


class Category(models.Model):
    name = models.CharField(max_length=200)
    cartoons = models.ForeignKey(Cartoon, related_name="categories", blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return u"%s %s" % (self.name)
