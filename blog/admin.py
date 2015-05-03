from django.contrib import admin
from .models import Authorship, Blog

# Register your models here.
class AuthorshipInline(admin.TabularInline):
  model = Authorship
  extra = 1

class BlogAdmin(admin.ModelAdmin):
  inlines = (AuthorshipInline,)
  prepopulated_fields = {"slug": ("title",)}

admin.site.register(Blog, BlogAdmin)
