from django.shortcuts import render_to_response
from article.models import Article
# for sessions and cookies
from django.http import HttpResponse

# for "create" view
from forms import ArticleForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

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


# for create Article
def create(request):
    # if user filled in the form (created article) and pressed "post"
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/all')
    # if user is visiting the page to create article - display blank form
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form
    return render_to_response('create_article.html', args)


def like_article(request, article_id):
    # if this is valid url
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)