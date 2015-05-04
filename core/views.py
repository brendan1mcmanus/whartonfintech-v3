from django.shortcuts import render
from blog.models import Blog

# Create your views here.
def home(request):
  blog = Blog.objects.filter(published=True).latest('dateline')
  return render(request, 'pages/home.html', {
    'menu_context': ('home',),
    'blog': blog,
    'is_homepage': True,
  })

def about_us(request):
  return render(request, 'pages/about.html', {
    'menu_context': ('about-us','about-us',),
  })

def board(request):
  return render(request, 'pages/board.html', {
    'menu_context': ('about-us','board',),
  })
