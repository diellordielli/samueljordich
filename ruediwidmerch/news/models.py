# -*- coding: utf-8 -*-
from django.db import models

from ..illustration.models import Illustration


# Create your models here.
class News(models.Model):
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
    text = models.TextField()
    date = models.DateTimeField()
    featured = models.BooleanField(default=False)
    images = models.ManyToManyField(Illustration, related_name="news", blank=True)

    class Meta:
        verbose_name_plural = "News"
        ordering = ['-date']

    def year(self):
        return self.date.strftime('%Y')

    def __unicode__(self):
        return u"%s %s" % (self.title, self.text)
