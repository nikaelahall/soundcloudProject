from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import soundcloud


class songSc(models.Model):
    client = soundcloud.Client(client_id='1127f01b608967f71cd5b142397ce03f', client_secret='128bc403986db5f60139d8c72e7d08f6', username='nikaela_hall@hotmail.co.nz', password='armbrosiamaid')
    data = client.get('/users/4847051/tracks')
    for track in data:
        title = models.CharField(max_length=255)
        track.title = title
        permalink_url = models.CharField(max_length=255)
        track.permalink_url = permalink_url


def create_song_list(sender, instance, created, **kwargs):
    if created:
        prof, created = songSc.objects.get_or_create(user=instance)

post_save.connect(create_song_list, sender=User)