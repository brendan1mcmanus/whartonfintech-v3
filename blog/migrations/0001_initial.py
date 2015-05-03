# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authorship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('author', models.ForeignKey(to='author.Author')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('text', models.TextField()),
                ('dateline', models.DateField()),
                ('banner_image', models.ImageField(upload_to=b'article-banners', blank=True)),
                ('published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('authors', models.ManyToManyField(related_name='blogs', through='blog.Authorship', to='author.Author')),
            ],
        ),
        migrations.AddField(
            model_name='authorship',
            name='blog',
            field=models.ForeignKey(related_name='authorship', to='blog.Blog'),
        ),
    ]
