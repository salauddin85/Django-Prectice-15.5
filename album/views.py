
# Create your views here.
from django.shortcuts import render,redirect
from .forms  import AlbumForm
from album.models import Album
from  musician.models import Musician
# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('albumpage')
    else:
        album_form = AlbumForm()
    return render(request,'album.html',{'form':album_form})


def edit_album(request,id):
    data = Album.objects.get(pk=id)
    # print(data.AlbumName)
    album_form = AlbumForm(instance = data)
    if request.method == 'POST':
        album_form = AlbumForm(request.POST,instance=data)
        if album_form.is_valid():
            album_form.save()
            return redirect('homepage')
    
    return render(request,'edit_album.html',{'form':album_form})




def delete_album(request,id):
    musician = Musician.objects.get(pk=id)
    musician.delete()
    return redirect ('homepage')
  