# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.functional import cached_property

import markdown
from django.utils.html import strip_tags
from markdown.extensions.toc import TocExtension
import re

#from django.utils.six import python_2_unicide_compatible

# Create your models here.

def generate_rich_content(value):
    md = markdown.Markdown(
        extensions=[
            "markdown.extensions.extra",
            "markdown.extensions.codehilite",
            TocExtension(slugify=slugify),
        ]
    )
    content = md.convert(value)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    toc = m.group(1) if m is not None else ""
    return {"content": content, "toc": toc}

class Category(models.Model):
    name = models.CharField("category", max_length=100)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField("tag", max_length=100)

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length = 200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    views = models.PositiveIntegerField(default=0)
    img = models.ImageField(default=0)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = verbose_name
        ordering = ["-created_time"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})

    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        md = markdown.Markdown(
            extensions=["markdown.extensions.extra", "markdown.extensions.codehilite",]
        )
        self.excerpt = strip_tags(md.convert(self.body))[:500]
        super().save(*args, **kwargs)


    @property   
    def toc(self):
        return self.rich_content.get("toc", "")
 
    @property
    def body_html(self):
        return self.rich_content.get("content", "")
 
    @cached_property
    def rich_content(self):
        return generate_rich_content(self.body)