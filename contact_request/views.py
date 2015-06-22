from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from ipware import ip
from .forms import ContactRequestForm

# Create your views here.
def contact(request):
  if request.method == 'POST': # If the form has been submitted...
    contact_request_form = ContactRequestForm(request.POST) # A form bound to the POST data
    if contact_request_form.is_valid(): # All validation rules pass
      contact_request = contact_request_form.save(commit=False)
      contact_request.url = request.POST.get('current_path','')
      contact_request.ip_address = ip.get_real_ip(request) if not settings.DEBUG else ip.get_ip(request)  # Inspired by http://stackoverflow.com/a/16203978
      contact_request.save()
      messages.success(request, 'Thanks for your message. You\'ll hear from us soon!')
      return redirect(contact_request.url or 'home') # Redirect after POST
  else:
    contact_request_form = ContactRequestForm(initial={'current_path':request.GET.get('current_path',request.build_absolute_uri())}) # An unbound form
  return render(request, 'contact_request/contact_page.html', {
    'contact_request_form': contact_request_form,
    'noindex': True,
  })
