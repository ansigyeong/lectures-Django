from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html')


def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Article()
    article.title = request.GET.get('title')
    article.content = request.GET.get('content')
    article.save()
    return redirect('/articles/')

def detail(request, pk):
    article = Article.objects.get(pk=pk) # 필드 이름 = 내부 함수에서 정의된 이름
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
    
