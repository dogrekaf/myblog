# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.CharField(max_length=200)
    body=models.TextField()
    pub_date=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=('-pub_date',)
    def __unicode__(self):
        return self.title
