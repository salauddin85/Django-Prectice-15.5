from django.db import models
from album.models import Album
# Create your models here.
class Musician(models.Model):
      FirstName = models.CharField(max_length=50)
      LastName  = models.CharField(max_length=50)
      Email = models.EmailField()
      Phone = models.CharField(max_length=11)
      InstrumentType = models.CharField(max_length=50)
      album = models.ForeignKey(Album,on_delete=models.CASCADE,null=True,blank=True)

      def __str__(self) -> str:
            return f'{self.FirstName}{self.LastName}'