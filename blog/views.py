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

  authors = blog.get_authors()
  return render(request, 'blog/post.html', {
    'blog': blog,
    'authors': authors,
    'menu_context': ('blog',),
  })
