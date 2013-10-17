from django.conf.urls import patterns, include, url
from django.contrib import admin
from index.views import events, registry
admin.autodiscover()

#Development only
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', include('index.urls')), # domain.com/
    url(r'^events/', events), # domain.com/events/
    url(r'^registry/', registry), # domain.com/registry/
    url(r'^gallery/', include('gallery.urls')), # domain.com/gallery/
    url(r'^admin/', include(admin.site.urls)), # domain.com/admin/
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
