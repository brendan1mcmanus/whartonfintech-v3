from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'pages/home.html', {
    'menu_context': ('home',),
    'is_homepage': True,
  })
