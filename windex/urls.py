from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

#Development only
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^$', include('index.urls')),
    url(r'^events/', include('index.urls')), 
    url(r'^gallery/', include('gallery.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
