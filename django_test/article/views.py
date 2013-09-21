from django.http import HttpResponse
# helper function that uses settings.py to find templates and get them
from django.template.loader import get_template
# templates have a Context object to insert data we have generated to the template
from django.template import Context

def hello(request):
    name = "Mike"
    html = "<html><body>Hi %s welcome! </body></html>" % name
    return HttpResponse(html)

def hello_template(request):
    name = "Mike"
    t = get_template('hello.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)