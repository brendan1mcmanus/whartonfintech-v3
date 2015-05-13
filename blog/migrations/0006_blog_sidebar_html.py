# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_sidebar_first'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='sidebar_html',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
