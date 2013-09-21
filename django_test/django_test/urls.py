from django.conf.urls import patterns, include, url
#from article.views import HelloTemplate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# this will let Django look through all of our Model in this project
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^articles/', include('article.urls')),  # ! w/o $
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^django_test/', include('django_test.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # tutorial 1.
    #   url(r'^hello/$', 'article.views.hello'),
    #   url(r'^hello_template/$', 'article.views.hello_template'),
    #   url(r'^hello_template_simple/$', 'article.views.hello_template_simple'),
    #   url(r'^hello_class_view/$', HelloTemplate.as_view()),
)
