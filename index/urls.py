from django.conf.urls import patterns, include, url
from index import views

urlpatterns = patterns('',
    # domain.com/
    url(r'^$', views.index, name='index'),
    # domain.com/events/
    url(r'^events/', views.events, name='events'),
)
