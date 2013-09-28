from django.db import models

class Image(models.Model):
  img = models.ImageField(upload_to='images/', name='Image')
  date = models.DateTimeField(auto_now_add=True)

