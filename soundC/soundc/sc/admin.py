from django.contrib import admin
from .models import songSc


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'permalink_url']

admin.site.register(songSc, PostAdmin)
