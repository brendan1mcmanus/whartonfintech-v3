# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
        ('blog', '0002_auto_20150504_1139'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='file_uploads',
            field=models.ManyToManyField(related_name='blogs', to='file_upload.FileUpload'),
        ),
    ]
