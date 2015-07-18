from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render
from .models import Blog

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

def post(request, slug):
  try:
    blog = Blog.objects.get(slug=slug)
  except Blog.DoesNotExist:
    raise Http404("Blog does not exist")

  is_authenticated = request.GET.get('password') == blog.password
  is_staff = request.user.is_staff

  if not blog.published:
    if is_authenticated:
      messages.error(request, '<p><strong>Warning!</strong> This blog is unpublished, and the public cannot see it. You are seeing this only because you have been given a <strong>private link</strong> to preview this post.</p><p><strong>Please do not share this link!</strong></p>')
    elif is_staff:
      messages.error(request,'<p><strong>Warning!</strong> This blog is unpublished, and the public cannot see it. You are seeing this only because you are logged in as a staff member.</p><p>Want to share this unpublished post with someone who isn\'t a staff member? Use <a href="{0}">this secure link</a>. <strong>Share it wisely.</strong></p>'.format(blog.get_private_url()))
    else:
      raise Http404("Blog is unpublished")

  authors = blog.get_authors()
  return render(request, 'blog/post.html', {
    'blog': blog,
    'authors': authors,
    'menu_context': ('blog',),
  })
