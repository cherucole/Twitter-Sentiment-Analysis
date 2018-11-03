from django.db import models
from django.conf import settings

# Create your models here.


class Sentiments(models.Model):
    query = models.CharField(
        max_length=150, default='Input #hashtag')

    def __str__(self):
        return self.query
