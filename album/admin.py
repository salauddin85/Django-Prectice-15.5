from django.contrib import admin

# Register your models here.
from .models import Album
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('AlbumName', 'album_release_date', 'Rating')
admin.site.register(Album)