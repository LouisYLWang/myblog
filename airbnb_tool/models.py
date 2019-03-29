# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Airbnb_tools(models.Model):
    url = models.URLField(blank=True)
    