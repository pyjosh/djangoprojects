from django.shortcuts import render_to_response
from article.models import Article, Comment
# for sessions and cookies
from django.http import HttpResponse

# for "create" view
from forms import ArticleForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone

from haystack.query import SearchQuerySet


import logging
logger = logging.getLogger(__name__)

def articles(request):
    logger.info("foo")
    # this on is stored in cookies
    language = 'en-gb'
    # this one is stored in session
    session_language = 'en-gb'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args = {}
    args.update(csrf(request))

    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render_to_response('articles.html', args)


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
        # request.FILES - to get uploaded files
        form = ArticleForm(request.POST, request.FILES)
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

#
# for comments
#
# INPUT - Add comment
# OUT 1 - page to add comment
# OUT 2 - POST action and redirection to article
def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)

    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            # save this frm but do NOT push anything into db
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            # RELATIONSHIP: relate this COMMENT with correcponding ARTICLE
            c.article = a
            c.save()

            return HttpResponseRedirect('/articles/get/%s' % article_id)

    # if this is not the POST method - so the first time we are seeing this
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))

    args['article'] = a
    args['form'] = f

    return render_to_response('add_comment.html', args)


#
# for whoosh search
#
def search_titles(request):
    articles = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))

    return render_to_response('ajax_search.html', {'articles': articles})