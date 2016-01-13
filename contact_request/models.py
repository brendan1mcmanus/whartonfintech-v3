from django.db import models

# Create your models here.
class ContactRequest(models.Model):
  PURPOSE_CHOICES = (
    ('', 'Where should we direct your message?'),
    ('FinTech Companies', (
      (1, 'Come to campus'),
      (2, 'Share ideas with students'),
      (3, 'Sponsor an independent study project'),
      (4, 'Recruit talent'),
      (5, 'Distribute job postings'),
      (6, 'Become a Wharton FinTech Sponsor'),
    )),
    ('Other',(
      (7, 'Author a blog post'),
      (8, 'Press Inquiries'),
      (9, 'Promote an event to Wharton FinTech members'),
      (10, 'Share information with Wharton FinTech members'),
    )),
    ('Feedback',(
      (11, 'General comments'),
      (12, 'Report an issue with the website'),
    )),
  )

  TO_EMAILS = {
     1: ['Neha Goel <nehagoel@wharton.upenn.edu>'],
     2: ['Neha Goel <nehagoel@wharton.upenn.edu>'],
     3: ['Neha Goel <nehagoel@wharton.upenn.edu>'],
     4: ['Aditya Goel <adityago@wharton.upenn.edu>'],
     5: ['Aditya Goel <adityago@wharton.upenn.edu>'],
     6: ['Uday Seth <useth@wharton.upenn.edu>'],
     7: ['Matthew Applegate <apmatt@wharton.upenn.edu>'],
     8: ['Matthew Applegate <apmatt@wharton.upenn.edu>'],
     9: ['Matthew Applegate <apmatt@wharton.upenn.edu>'],
    10: ['Matthew Applegate <apmatt@wharton.upenn.edu>'],
    11: ['Uday Seth <useth@wharton.upenn.edu>'],
    12: ['Brendan McManus <bmcmanus@wharton.upenn.edu>'],
  }
  CC_EMAILS = {
     1: ['Uday Seth <useth@wharton.upenn.edu>', 'Irfanali Manji <imanji@wharton.upenn.edu>'],
     2: ['Uday Seth <useth@wharton.upenn.edu>', 'Irfanali Manji <imanji@wharton.upenn.edu>'],
     3: ['Uday Seth <useth@wharton.upenn.edu>', 'Irfanali Manji <imanji@wharton.upenn.edu>'],
     4: ['Uday Seth <useth@wharton.upenn.edu>', 'Irfanali Manji <imanji@wharton.upenn.edu>'],
     5: ['Uday Seth <useth@wharton.upenn.edu>', 'Irfanali Manji <imanji@wharton.upenn.edu>'],
     6: [],
     7: ['Uday Seth <useth@wharton.upenn.edu>', 'Irfanali Manji <imanji@wharton.upenn.edu>'],
     8: ['Uday Seth <useth@wharton.upenn.edu>', 'Irfanali Manji <imanji@wharton.upenn.edu>'],
     9: ['Uday Seth <useth@wharton.upenn.edu>', 'Irfanali Manji <imanji@wharton.upenn.edu>'],
    10: ['Uday Seth <useth@wharton.upenn.edu>', 'Irfanali Manji <imanji@wharton.upenn.edu>'],
    11: [],
    12: ['Uday Seth <useth@wharton.upenn.edu>'],
  }

  name = models.CharField(max_length=128)
  email = models.EmailField(max_length=128)
  purpose = models.SmallIntegerField(choices=PURPOSE_CHOICES)
  message = models.TextField()
  url = models.URLField(max_length=254, blank=True)
  ip_address = models.GenericIPAddressField(null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  edited = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created']
