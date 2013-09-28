from django.shortcuts import render
from index.models import Event, Registry

def index(request):
  return render(request, 'index/index.html')
