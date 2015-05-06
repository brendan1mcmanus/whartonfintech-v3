from django.contrib import admin
from django.utils.html import format_html
from .models import FileUpload

# Register your models here.
class FileUploadAdmin(admin.ModelAdmin):
  list_display = ('title', 'file_url', 'linked_blogs',)

  def file_url(self, obj):
    return format_html('<a href="{0}" target="_blank">{0}</a>', obj.file.url)

  def linked_blogs(self, obj):
    blogs = obj.blogs.all()
    if len(blogs) > 1:
      return format_html('<ul>{}</ul>'.format(''.join([format_html('<li><a href="{0}" target="_blank">{1}</a></li>',blog.get_absolute_url(),blog.title) for blog in blogs])))
    elif len(blogs) == 1:
      blog = blogs.first()
      return format_html('<a href="{0}" target="_blank">{1}</a>',blog.get_absolute_url(),blog.title)
    else:
      return '-'

admin.site.register(FileUpload, FileUploadAdmin)
