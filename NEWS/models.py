from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    rating = models.FloatField(default=0)
    post_title = models.CharField(max_length=255)
    post_text = models.TextField()
