from crispy_forms import helper, layout
from django import forms
from .models import ContactRequest

class ContactRequestForm(forms.ModelForm):
  current_path = forms.URLField(max_length=254, required=False, widget=forms.HiddenInput())

  class Meta:
    model = ContactRequest
    fields = [
      'purpose',
      'message',
      'name',
      'email',
    ]

  def __init__(self, *args, **kwargs):
    super(ContactRequestForm, self).__init__(*args, **kwargs)
    self.helper = helper.FormHelper()

    self.helper.form_tag = False
    self.helper.label_class = 'col-sm-2'
    self.helper.field_class = 'col-sm-10'
    self.helper.layout = helper.Layout(
      'current_path',
      'purpose',
      layout.Field('message', placeholder="Please send us your comments or questions!"),
      layout.Field('name',    placeholder="Your full name"),
      layout.Field('email',   placeholder="Your email address"),
    )
