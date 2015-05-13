# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sidebar_first',
            field=models.BooleanField(default=False, help_text=b'Leave unchecked on most blog posts. Useful if the sidebar should be presented before the blog on a mobile display. Sidebar will still appear to the right of the blog post on regular displays.', verbose_name=b'Show sidebar HTML first, before blog post'),
        ),
    ]
