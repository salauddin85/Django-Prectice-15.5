from django import forms
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        # fields = '__all__'
        exclude = [
            "album_release_date",
        ]
        
        