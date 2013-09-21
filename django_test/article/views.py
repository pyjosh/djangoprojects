from django.shortcuts import render_to_response
from article.models import Article

def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all()})

def article(request, article_id):
    return render_to_response('articles.html', {'article': Article.objects.get(id=article_id)})
