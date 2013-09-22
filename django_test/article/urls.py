from django.conf.urls import patterns, include, url
from api import ArticleResource

article_resource = ArticleResource()

urlpatterns = patterns('',
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'article.views.article'),

    # for session language
    url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language'),

    # create new article
    url(r'^create/$', 'article.views.create'),

    # for "likes" update
    url(r'^like/(?P<article_id>\d+)/$', 'article.views.like_article'),

    # for comments
    url(r'^add_comment/(?P<article_id>\d+)/$', 'article.views.add_comment'),

    # TODO: for search - use to receive a msg using ajax call from js
    url(r'^search/$', 'article.views.search_titles'),

    # for API access (!) w/o '$' !!!
    url(r'^api/', include(article_resource.urls)),
)