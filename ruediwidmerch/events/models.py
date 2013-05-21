# -*- coding: utf-8 -*-
from django.db import models


# Create your models here.
class Event(models.Model):
    title = models.TextField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Events"
        ordering = ['-date']

    def month(self):
        return self.date.strftime('%B %Y')

    def __unicode__(self):
        return u"%s %s" % (self.title, self.text)
