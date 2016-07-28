from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^about/$', views.GreetingView.as_view(greeting="G'day")),
    url(r'^$', views.songlist, name='songList'),
]