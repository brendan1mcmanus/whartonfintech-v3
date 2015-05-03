from django.db import models

# Create your models here.
class Author(models.Model):
  first_name = models.CharField(max_length=32)
  last_name = models.CharField(max_length=32)
  slug = models.SlugField()
  avatar = models.ImageField(upload_to="authors")
  bio = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)

  def full_name(self):
    full_name = '%s %s' % (self.first_name, self.last_name)
    return full_name.strip()

  def __unicode__(self):
    return self.full_name()
