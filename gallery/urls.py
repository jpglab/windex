from django.conf.urls import patterns, include, url
from gallery import views

urlpatterns = patterns('',
    # domain.com/gallery
<<<<<<< HEAD
    url(r'^$', views.gallery, name='gallery'),
=======
    url(r'^$', views.gallary, name='gallery'),
>>>>>>> 513824b1b9ca410b5405aca51d209019b9a2af91
)
