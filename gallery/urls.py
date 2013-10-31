from django.conf.urls import patterns, include, url
from gallery.views import gallery, album

urlpatterns = patterns('',
    url(r'^$', gallery),
    url(r'^(?P<req_album>.+)/', album),
)
