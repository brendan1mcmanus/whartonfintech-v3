from django.db import models
from django.core.urlresolvers import reverse
from random import choice
from urllib import urlencode

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=128)
  slug = models.SlugField(max_length=100)
  description = models.TextField()
  text = models.TextField()
  dateline = models.DateField()
  authors = models.ManyToManyField('author.Author', through='blog.Authorship', related_name='blogs')
  banner_image = models.ImageField(upload_to='article-banners', blank=True)
  file_uploads = models.ManyToManyField('file_upload.FileUpload', related_name='blogs')
  published = models.BooleanField(default=False)
  password = models.CharField(max_length=24, editable=False)
  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.password:
      self.password = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(Blog._meta.get_field('password').max_length)])
    super(Blog, self).save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse('blog:post', args=[self.slug])

  def get_private_url(self):
    return self.get_absolute_url() + '?' + urlencode({
      'password': self.password,
    })

  def get_authors(self):
    return self.authors.order_by('authorship')

  def byline(self):
    authors = self.get_authors()
    return ' and '.join([author.full_name() for author in authors]) if authors else 'Wharton FinTech'


class Authorship(models.Model):
  author = models.ForeignKey('author.Author')
  blog = models.ForeignKey('blog.Blog', related_name='authorship')
  order = models.IntegerField()

  class Meta:
    ordering = ('order',)
