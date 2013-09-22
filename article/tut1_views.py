# --1.--  hello
from django.http import HttpResponse

# --2.--  hello_template
# helper function that uses settings.py to find templates and get them
from django.template.loader import get_template
# templates have a Context object to insert data we have generated to the template
from django.template import Context

# --3.--  HelloTemplate
from django.views.generic.base import TemplateView

# --4.-- hello_template_simple
from django.shortcuts import render_to_response

def hello(request):
    name = "Mike"
    html = "<html><body>Hi %s welcome! </body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Mike"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def hello_template_simple(request):
    name = "Mike"
    return render_to_response('hello.html', {'name': name})

class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Mike'
        return context