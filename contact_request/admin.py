from django.contrib import admin
from .models import ContactRequest

class ContactRequestAdmin(admin.ModelAdmin):
  list_display = ('name','email','url','created',)
  readonly_fields = ('name','email','message','url','ip_address','created',)

admin.site.register(ContactRequest, ContactRequestAdmin)
