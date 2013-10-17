from django.db import models

class Event(models.Model):
  date_time = models.DateTimeField()
  title = models.CharField(max_length=32)
  address_name = models.CharField(max_length=32)
  street = models.CharField(max_length='100')
  city = models.CharField(max_length='100')
  state = models.CharField(max_length='2')
  zip = models.CharField(max_length='5')
  phone = models.CharField(max_length='20')
  map = models.TextField(blank=True)
  info = models.TextField(blank=True)
  
  def __unicode__(self):
    return self.title

class Registry(models.Model):
  store = models.CharField(max_length='32')
  url = models.URLField()
  info = models.TextField()

  def __unicode__(self):
    return self.store
