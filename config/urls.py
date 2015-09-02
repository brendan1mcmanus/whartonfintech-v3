# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

# Comment the next two lines to disable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',  # noqa
    # Django Admin (Comment the next line to disable the admin)
    url(r'^admin/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("whartonfintech.users.urls", namespace="users")),
    url(r'^accounts/', include('allauth.urls')),
)

# Custom URLs
urlpatterns += patterns('core.views',
  url(r'^$', 'home', name='home'),
  url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name="about"),
  url(r'^blog/', include("blog.urls", namespace="blog")),
  url(r'^about/fintech-club/$', 'about_us', name='about-us'),
  url(r'^about/board/$', 'board', name='board'),
  url(r'^about/sponsors/$', 'sponsors', name='sponsors'),
  url(r'^join/$', 'join', name='join'),
  url(r'^legal/$', 'legal', name='legal'),
  # Redirect pre-existing URLs to maintain backwards compatibility with inbound links.
  url(r'^about/contact-us/$', 'contact_us_redirect'),
  # Capture all URLs that with index.html
  url(r'^index.html$', 'index_redirect'),
  url(r'^(?P<url>.+/)index.html$', 'index_redirect'),
)

urlpatterns += patterns('contact_request.views',
  url(r'^contact/$', 'contact', name='contact'),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
