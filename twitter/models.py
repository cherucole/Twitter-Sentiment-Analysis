from django.conf import settings
from django.db import models


# Create your models here.
class SentimentsTwitterHashtag(models.Model):
    topic = models.CharField(max_length=128)
    sample_size = models.CharField(max_length=100)
    postive_count = models.IntegerField(max_length=100)
    neutral_count = models.IntegerField(max_length=100)
    negative_count = models.IntegerField(max_length=100)
    neutral_tweets = models.TextField(max_length=100)
    negative_tweets = models.TextField(max_length=100)
    postive_tweets = models.TextField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.topic
