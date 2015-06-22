from django.db import models

# Create your models here.
class ContactRequest(models.Model):
  name = models.CharField(max_length=128)
  email = models.EmailField(max_length=128)
  message = models.TextField()
  url = models.URLField(max_length=254, blank=True)
  ip_address = models.GenericIPAddressField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created']
