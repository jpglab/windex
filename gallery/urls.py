from django.conf.urls import patterns, include, url
from gallary import views

urlpatterns = patterns('',
    # domain.com/gallary
    url(r'^$', views.gallary, name='gallary'),
)
