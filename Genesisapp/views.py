from django.shortcuts import render

# Create your views here.
def details(request):
    return render(request, 'blog-details.html')

def home(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def service(request):
    return render(request, 'services-details.html')

def starter(request):
    return render(request, 'starter-page.html')
