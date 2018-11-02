from django.db import models
from django.conf import settings

# Create your models here.


class sentiments(models.Model):
    query = models.CharField(
        required=True, max_length=150, label='Input #hashtag')

    def __str__(self):
        return self.query
