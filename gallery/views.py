from django.shortcuts import render
from gallery.models import Image, Album

def gallery(request):
  album_list = Album.objects.all()
  context = {'album_list': album_list}
  return render(request, 'gallery/gallery.html', context)
