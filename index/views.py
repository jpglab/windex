from django.http import HttpResponse
from django.shortcuts import render
from index.models import Event, Registry

def index(request):
  return render(request, 'index/index.html')

def rsvp(request):
  return HttpResponse('RSVP details')

def events(request):
  event_list = Event.objects.order_by('-date_time')
  context = {'event_list': event_list}
  return render(request, 'index/events.html', context)

def registry(request):
  reg_list = Registry.objects.all()
  context = {'reg_list': reg_list}
  return render(request, 'index/registry.html', context)
