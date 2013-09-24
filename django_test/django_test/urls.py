from django.conf.urls import patterns, include, url
#from article.views import HelloTemplate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# this will let Django look through all of our Model in this project
admin.autodiscover()


from django_test.forms import ContactForm1, ContactForm2, ContactForm3
from django_test.views import ContactWizard

urlpatterns = patterns('',
    url(r'^articles/', include('article.urls')),  # ! w/o $
    url(r'^accounts/', include('userprofile.urls')),  # ! w/o $

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

    url(r'^accounts/login/$', 'django_test.views.login'),
    url(r'^accounts/auth/$', 'django_test.views.auth_view'),
    url(r'^accounts/logout/$', 'django_test.views.logout'),
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),

    url(r'^accounts/register/$', 'django_test.views.register_user'),
    url(r'^accounts/register_success/$', 'django_test.views.register_success'),


    url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
)
