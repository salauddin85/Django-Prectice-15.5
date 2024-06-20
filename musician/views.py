from django.shortcuts import render,redirect
from .forms import MusicianForm
from .import models
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('homepage')
    else:
        form  = MusicianForm()
    return render(request,'musician.html',{'form':form})


def musician_edit(request,id):
    musician = models.Musician.objects.get(pk=id)
    musician_form = MusicianForm(instance=musician)
    if request.method == 'POST':
        musician_form  = MusicianForm(request,instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('homepage')
    return render(request,'musician.html',{'form':musician_form})