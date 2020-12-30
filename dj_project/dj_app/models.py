from django.db import models
from django.utils import timezone
from datetime import datetime
# Create your models here.
class post (models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=datetime.now)
    published_date = models.DateTimeField(blank=True, null=True)

class comment (models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)