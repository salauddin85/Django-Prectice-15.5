from django.db import models
# from musician.models import Musician

class Album(models.Model):
    
    AlbumName = models.CharField(max_length=50,default=None)
    album_release_date  = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    CHOICE = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    Rating = models.CharField(max_length=20,choices=CHOICE,null=True)

    def __str__(self) -> str:
        return f'{self.AlbumName}'
   