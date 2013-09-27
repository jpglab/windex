from django.http import HttpResponse

def index(request):
  return HttpResponse('<h2>Welcome to Windex!</h2><br/>This is the index app\'s root url.')
