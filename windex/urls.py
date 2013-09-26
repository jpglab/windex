from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('index.urls')),
    url(r'^gallary/', include('gallary.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
