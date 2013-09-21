from django.shortcuts import render_to_response
from article.models import Article
# for sessions and cookies
from django.http import HttpResponse


def articles(request):
    # this on is stored in cookies
    language = 'en-gb'
    # this one is stored in session
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render_to_response('articles.html',
        {'articles': Article.objects.all(),
        'language' : language,
        'session_language': session_language}
        )

def article(request, article_id):
    return render_to_response('article.html', {'article': Article.objects.get(id=article_id)})



def language(request, language='en-gb'):
    # this is rendered to the browser window - will print this on the page
    respone = HttpResponse("seting language to %s " % language)

    # COOKIE --> RESPONSE
    respone.set_cookie('lang', language)
    # SESSION --> REQUEST
    request.session['lang'] = language

    return respone