from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'aricle.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'aricle.views.article'),
)