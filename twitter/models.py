from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.


# Create your models here.
class Profile(models.Model):
    # photo = models.ImageField(upload_to='image/', null=True)
    # email = models.CharField(max_length=30, null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, default=1)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.save()

    class Meta:
        ordering = ['user']

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains=name)
        return profile

    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile


class SentimentsTwitterHashtag(models.Model):
    topic = models.CharField(max_length=128)
    sample_size = models.CharField(max_length=100)
    postive_count = models.IntegerField()
    neutral_count = models.IntegerField()
    negative_count = models.IntegerField()
    neutral_tweets = models.TextField(max_length=100)
    negative_tweets = models.TextField(max_length=100)
    postive_tweets = models.TextField(max_length=100)
    publication_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.topic

    @classmethod
    def get_profile_reports(cls, profile):
        sentiments = SentimentsTwitterHashtag.objects.filter(user__pk=profile)
        return sentiments


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
