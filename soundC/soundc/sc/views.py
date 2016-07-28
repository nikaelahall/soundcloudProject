from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import songSc
from django.db import models
import soundcloud


def songlist(request):
    try:
        client = soundcloud.Client(client_id='1127f01b608967f71cd5b142397ce03f', client_secret='128bc403986db5f60139d8c72e7d08f6', username='nikaela_hall@hotmail.co.nz', password='armbrosiamaid')
        data = client.get('/users/4847051/tracks')
        for track in data:
            print(track.title, track.permalink_url)
    except Exception as err:
            print("test")
            print(err)
    return render(request, 'sc/song_list.html', {})


"""Testing"""""


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)
