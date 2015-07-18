from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogInlineEditForm

# Create your views here.
def index(request):
  blogs_list = Blog.objects.filter(published=True).order_by('-dateline')
  paginator = Paginator(blogs_list, 5)

  page = request.GET.get('page')
  try:
    blogs = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    blogs = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    blogs = paginator.page(paginator.num_pages)

  return render(request, 'blog/index.html', {
    'blogs': blogs,
    'menu_context': ('blog',),
  })

def post(request, slug, is_edit_page=False):
  try:
    blog = Blog.objects.get(slug=slug)
  except Blog.DoesNotExist:
    raise Http404("Blog does not exist")

  is_authenticated = request.GET.get('password') == blog.password
  is_staff = request.user.is_staff

  can_edit = is_authenticated or is_staff
  edit_mode = can_edit and is_edit_page
  blog_inline_edit_form = None
  if can_edit:
    if edit_mode:
      # Process form data.
      if request.method == 'POST': # If the form has been submitted...
        blog_inline_edit_form = BlogInlineEditForm(request.POST, instance=blog) # A form bound to the POST data
        if blog_inline_edit_form.is_valid(): # All validation rules pass
          blog_inline_edit_form.save()
          messages.success(request, 'Edits have been saved!')
          return redirect(blog.get_private_url()) # Redirect after POST
      else:
        blog_inline_edit_form = BlogInlineEditForm(instance=blog) # An unbound form
      # Display save link.
      messages.warning(request, '<p>You are editing this blog post.</p><p><a href="{0}" class="btn btn-warning" id="blog-inline-edit-form-submit">Save edits</a></p>'.format(blog.get_private_edit_url()))
    else:
      # Display edit link.
      if is_staff:
        messages.warning(request, '<p><strong>Alert!</strong> You can edit this, because you are logged in as a staff member.</p><p>Want to let someone who isn\'t a staff member edit this post? Use <a href="{0}">this secure link</a>. <strong>Share it wisely.</strong></p><p><a href="{0}" class="btn btn-warning">Edit this blog</a></p>'.format(blog.get_private_edit_url()))
      elif is_authenticated:
        messages.warning(request, '<p><strong>Alert!</strong> You can edit this, because you have been given a <strong>private link</strong> to edit this post.</p><p><strong>Please do not share this link!</strong></p><p><a href="{0}" class="btn btn-warning">Edit this blog</a></p>'.format(blog.get_private_edit_url()))

  if not blog.published:
    if is_staff:
      messages.error(request,'<p><strong>Warning!</strong> This blog is unpublished, and the public cannot see it. You are seeing this only because you are logged in as a staff member.</p><p>Want to share this unpublished post with someone who isn\'t a staff member? Use <a href="{0}">this secure link</a>. <strong>Share it wisely.</strong></p>'.format(blog.get_private_url()))
    elif is_authenticated:
      messages.error(request, '<p><strong>Warning!</strong> This blog is unpublished, and the public cannot see it. You are seeing this only because you have been given a <strong>private link</strong> to preview this post.</p><p><strong>Please do not share this link!</strong></p>')
    else:
      raise Http404("Blog is unpublished")

  authors = blog.get_authors()
  return render(request, 'blog/post.html', {
    'blog': blog,
    'authors': authors,
    'menu_context': ('blog',),
    'can_edit': can_edit,
    'edit_mode': edit_mode,
    'blog_inline_edit_form': blog_inline_edit_form,
  })
