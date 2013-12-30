from django.shortcuts import render
from models import Article, Category


def index(request):
    return render(request, 'blog/index.html', {
        'latest_articles': Article.objects.all()[:5],
        'categories': Category.objects.all()
    })


def article(request, slug):
    return render(request, 'blog/article.html', {
        'article': Article.objects.get(slug=slug),
        'categories': Category.objects.all()
    })