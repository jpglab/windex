from django.conf.urls import patterns, include, url
from gallery import views

urlpatterns = patterns('',
    # domain.com/gallery
    url(r'^$', views.gallary, name='gallery'),
)
