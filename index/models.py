from django.db import models

class Event(models.Model):
  date_time = models.DateTimeField()
  title = models.CharField(max_length=32)
  address = models.CharField(max_length='100')
  info = models.TextField()
  
  def __unicode__(self):
    return self.title

class Registry(models.Model):
  store = models.CharField(max_length='32')
  url = models.URLField()
  info = models.TextField()

  def __unicode__(self):
    return self.store
