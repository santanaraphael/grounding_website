from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def design(request):
    return render(request, 'design.html')
