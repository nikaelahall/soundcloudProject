from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class songSc(models.Model):
        title = models.CharField(max_length=255)
        permalink_url = models.CharField(max_length=255)


def create_song_list(sender, instance, created, **kwargs):
    if created:
        prof, created = songSc.objects.get_or_create(user=instance)

post_save.connect(create_song_list, sender=User)