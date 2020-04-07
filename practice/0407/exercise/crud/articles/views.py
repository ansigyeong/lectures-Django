from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def detail(request):
    return render(request, 'detail.html')