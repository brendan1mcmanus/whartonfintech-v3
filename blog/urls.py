from django.conf.urls import patterns, url

urlpatterns = patterns('',
  url(r'^$', 'blog.views.index', name='index'),
  url(r'^(?P<slug>.+)/$', 'blog.views.post', name='post'),
)
