# -*- coding: utf-8 -*-
from django.db import models

from ..illustration.models import Illustration


# Create your models here.
class Portrait(models.Model):
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

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    width = models.CharField(max_length=20, choices=IMAGE_WIDTH)
    height = models.CharField(max_length=20, choices=IMAGE_HEIGHT)
    images = models.ManyToManyField(Illustration, related_name="portraits", blank=True)

    class Meta:
        verbose_name_plural = "Portraits"

    def __unicode__(self):
        return u"%s %s %s" % (self.title, self.subtitle, self.description)
