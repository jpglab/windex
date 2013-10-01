from django.db import models

class Image(models.Model):
  path = models.ImageField(upload_to='images/', name='Image', null=False)
  caption = models.CharField(max_length=32, blank=False)
  date = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.caption

