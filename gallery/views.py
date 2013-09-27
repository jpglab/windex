from django.shortcuts import render
from gallery.models import Image

def gallery(request):
  #images = Image.objects.all()
  #template = 
  return render(request, 'gallery/gallery.html')
