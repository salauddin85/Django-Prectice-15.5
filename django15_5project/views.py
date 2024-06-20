from django.shortcuts import render,redirect
from  musician.models import Musician 

    
def home(request):
    data = Musician.objects.all()
    return render(request,'home.html',{'data':data})
