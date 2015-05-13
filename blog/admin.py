from django.contrib import admin
from django.utils.html import format_html
from .models import Authorship, Blog

# Register your models here.
class AuthorshipInline(admin.TabularInline):
  model = Authorship
  extra = 1

class FileUploadInline(admin.TabularInline):
  model = Blog.file_uploads.through
  extra = 1
  verbose_name = 'File upload'
  verbose_name_plural = 'File uploads'
  readonly_fields = ('file_upload_url',)

  def file_upload_url(self, obj):
    if hasattr(obj,'fileupload'):
      return format_html('<a href="{0}" target="_blank">{0}</a>', obj.fileupload.file.url)
    return '-'

class BlogAdmin(admin.ModelAdmin):
  fieldsets = (
    (None, {
      'fields': ('title', 'slug', 'description', 'text', 'dateline', 'banner_image', 'published')
    }),
    ('Customize Sidebar', {
      'classes': ('collapse',),
      'fields': ('sidebar_first', 'sidebar_html')
    }),
  )
  inlines = (AuthorshipInline,FileUploadInline,)
  prepopulated_fields = {"slug": ("title",)}
  exclude = ('file_uploads',)

admin.site.register(Blog, BlogAdmin)
