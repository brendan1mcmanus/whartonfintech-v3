from django.db import models

# Create your models here.
class FileUpload(models.Model):
  title = models.CharField(max_length=128)
  file = models.FileField(upload_to='uploads')
  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.title
