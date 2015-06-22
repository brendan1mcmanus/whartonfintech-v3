from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from email.utils import formataddr
from .models import ContactRequest

# todo: hook this up with celery in the future
def process_contact_requests(crid):
  contact_request = ContactRequest.objects.get(pk=crid)
  message_params = {
    'subject': 'Contact Request from WhartonFinTech.org',
    'body': render_to_string('contact_request/email_body.txt', {
      'contact_request': contact_request,
    }),
    'from_email': formataddr((contact_request.name,'no-reply@whartonfintech.org')),
    'to': ['contact@whartonfintech.org'],
    'bcc': ['contact_monitor@whartonfintech.org'],
    'headers': {
      'Reply-To': formataddr((contact_request.name,contact_request.email)),
    },
  }
  message = EmailMessage(**message_params)
  message.send(fail_silently=False)
