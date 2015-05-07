# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from random import choice


def generate_passwords(apps, schema_editor):
  Blog = apps.get_model("blog", "Blog")
  for blog in Blog.objects.all():
    blog.password = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(Blog._meta.get_field('password').max_length)])
    blog.save()

def ungenerate_passwords(apps, schema_editor):
  Blog = apps.get_model("blog", "Blog")
  for blog in Blog.objects.all():
    blog.password = 'xxxxxxxx'
    blog.save()

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_file_uploads'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='password',
            field=models.CharField(default='xxxxxxxx', max_length=24, editable=False),
            preserve_default=False,
        ),
        migrations.RunPython(generate_passwords, ungenerate_passwords),
    ]
