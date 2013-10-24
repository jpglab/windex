from django.db import models

class Album(models.Model):
  name = models.CharField(max_length=100, blank=False)
  description = models.TextField()
  key_image = models.ImageField(upload_to='images/album-thumbs/', name='Thumb', null=False)

  def __unicode__(self):
    return self.name


class Image(models.Model):
  album = models.ForeignKey(Album)
  file = models.ImageField(upload_to='images/', name='Image', null=False)
  caption = models.CharField(max_length=32, blank=False)
  date = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.caption

