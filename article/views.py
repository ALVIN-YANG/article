from django.shortcuts import render
from .models import Article
# Create your views here.


def article(request, code):
    print(code)
    article = Article.objects.first()
    return render(request, 'page.html', {'content': article.content, "title": article.title})