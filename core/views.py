from django.shortcuts import render, redirect
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

def sponsors(request):
  return render(request, 'pages/sponsors.html', {
    'menu_context': ('about-us','sponsors',),
  })

def join(request):
  return render(request, 'pages/join.html', {
    'menu_context': ('join',),
  })

def legal(request):
return render(request, 'pages/legal.html', {
  'menu_context': ('legal',),
})

def contact_us_redirect(request):
  return redirect('join', permanent=True)

def index_redirect(request, url=''):
  return redirect("/"+url, permanent=True)
