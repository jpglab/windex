from django.http import HttpResponse
from django.shortcuts import render
from index.models import Event, Registry

def index(request):
  return render(request, 'index/index.html')

def rsvp(request):
  return HttpResponse('RSVP details')

def events(request):
  event_list = Event.objects.order_by('-date')
  context = {'event_list': event_list}
  return render(request, 'index/events.html', context)
