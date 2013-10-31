import os
import windex.settings
from django.db import models
from PIL import Image as PIL_Image

def to_thumb(img):
  "Creates a thumbnail of an uploaded image."
  size = 480, 480

  #Split the ImageField's name and insert .thumb into it
  #Assign the filename to thumb_path to use when saving the final thumbnail image
  filename, ext = os.path.splitext(img.name)
  thumb_path = filename + '.thumb.jpg'

  #Open image associated with the ImageField
  i = PIL_Image.open(windex.settings.MEDIA_ROOT + img.name)

  #Create thumnail and safe it to the thumb_path
  i.thumbnail(size, PIL_Image.ANTIALIAS)
  i.save(windex.settings.MEDIA_ROOT + thumb_path, 'JPEG')


class Album(models.Model):
  name = models.CharField(max_length=100, blank=False)
  description = models.TextField()
  album_image = models.ImageField(upload_to='images/album-images/', null=False)
  album_thumb = models.ImageField(upload_to='images/album-images/', blank=True, editable=False)

  def __unicode__(self):
    return self.name

  def save(self):
    f, e = os.path.splitext(self.album_image.name)
    self.album_thumb = 'images/album-images/' + f.replace(' ','_')  + '.thumb.jpg'
    super(Album, self).save()
    to_thumb(self.album_image)


class Image(models.Model):
  album = models.ForeignKey(Album)
  date = models.DateTimeField(auto_now_add=True)
  caption = models.CharField(max_length=32, blank=False)
  image_image = models.ImageField(upload_to='images/image-images', null=False)
  image_thumb = models.ImageField(upload_to='images/image-images', blank=True, editable=False)

  def __unicode__(self):
    return self.caption

  def save(self):
    f, e = os.path.splitext(self.image_image.name)
    self.image_thumb = 'images/image-images/' + f.replace(' ','_')  + '.thumb.jpg'
    super(Image, self).save()
    to_thumb(self.image_image)
    
