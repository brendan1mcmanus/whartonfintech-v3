from crispy_forms import helper, layout
from django import forms
from .models import Blog

class BlogInlineEditForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = [
      'title',
      'text',
    ]

  def __init__(self, *args, **kwargs):
    super(BlogInlineEditForm, self).__init__(*args, **kwargs)

    # Todo: Remove when this issue is resolved (and add "type='hidden'" to layout.Field below): https://github.com/maraujop/django-crispy-forms/issues/344
    self.fields['title'].widget = forms.HiddenInput()
    self.fields['text'].widget = forms.HiddenInput()

    self.helper = helper.FormHelper()
    self.helper.form_tag = False
    self.helper.layout = helper.Layout(
      layout.Field('title'),
      layout.Field('text'),
    )
