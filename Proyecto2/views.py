from django.shortcuts import render, redirect  
from Proyecto2.forms import MusicForm  
from Proyecto2.models import Music

# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = MusicForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = MusicForm()  
    return render(request,'index.html',{'form':form})  
def index(request):  
    songs = Music.objects.all()  
    return render(request,"show.html",{'songs':songs})  

def edit(request, id):  
    song = Music.objects.get(id=id)  
    return render(request,'edit.html', {'song':song})  

def update(request, id):  
    song = Music.objects.get(id=id)  
    form = MusicForm(request.POST, instance = song)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'song': song})  
def destroy(request, id):  
    song = Music.objects.get(id=id)  
    song.delete()  
    return redirect("/")  
