# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_request', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactrequest',
            name='purpose',
            field=models.SmallIntegerField(default=1, choices=[(b'', b'Where should we direct your message?'), (b'FinTech Companies', ((1, b'Come to campus'), (2, b'Share ideas with students'), (3, b'Sponsor an independent study project'), (4, b'Recruit talent'), (5, b'Distribute job postings'), (6, b'Become a Wharton FinTech Sponsor'))), (b'Other', ((7, b'Author a blog post'), (8, b'Press Inquiries'), (9, b'Promote an event to Wharton FinTech members'), (10, b'Share information with Wharton FinTech members'))), (b'Feedback', ((11, b'General comments'), (12, b'Report an issue with the website')))]),
            preserve_default=False,
        ),
    ]
