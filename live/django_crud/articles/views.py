from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    article = Article.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Article()
    article.title = request.GET.get('title')
    article.content= request.GET.get('content')
    article.save()
    # return render(request, 'articles/create.html')
    return redirect('/articles/')