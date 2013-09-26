from django.conf.urls import patterns, include, url
from index import views

urlpatterns = patterns('',
    # domain.com/
    url(r'^$', views.index, name='index'),
)
