# -*- coding: utf-8 -*-
from django.db import models

from ..cartoons.models import Cartoon


# Create your models here.
class Column(models.Model):
    IMAGE_WIDTH = (
        ('1', '1'),
        ('2', '2'),
        ('4', '4'),
    )

    IMAGE_HEIGHT = (
        ('1', '%'),
        ('2', '%'),
        ('3', '%'),
        ('4', '%'),
    )

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    magazine = models.CharField(max_length=100)
    date = models.DateTimeField()
    text = models.TextField()
    images = models.ManyToManyField(Cartoon, related_name="columns", blank=True)

    class Meta:
        verbose_name_plural = "Columns"
        ordering = ['-date']

    def __unicode__(self):
        return u"%s %s %s" % (self.title, self.subtitle, self.text)
