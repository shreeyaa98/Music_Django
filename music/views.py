from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Album
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    all_albums=Album.objects.all()
    context = {'all_albums':all_albums}
    return render(request,'music/index.html',context)

def detail(request,album_id):
    album=get_object_or_404(Album,id=album_id) #eliminates need of try except block
    return render(request,'music/detail.html',{'album':album})

def favorite(request,album_id):
    album=get_object_or_404(Album,id=album_id) 
    try:
        selected_song=album.song_set.get(id=request.POST['song'])
    except(KeyError,Song.DoesNotExist): #Key Error that is error message displayed on the top
        return render(request,'music/detail.html',{
            'album':album,
            'error_message':"You did not Select Song"
            })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        print(selected_song,selected_song.is_favourite)
        return render(request,'music/detail.html',{'album':album})