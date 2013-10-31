from django.shortcuts import render
from gallery.models import Image, Album
from django.http import Http404


def gallery(request):
  album_list = Album.objects.all()
  context = {'album_list': album_list}
  return render(request, 'gallery/gallery.html', context)

def album(request, req_album):
  image_list = Image.objects.filter(album__name=req_album.title())
  context = {'image_list': image_list, 'album_name': req_album}
  return render(request, 'gallery/album.html', context)

