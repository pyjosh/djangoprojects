from django.http import HttpResponse


def hello(request):
    name = "Mike"
    html = "<html><body>Hi %s welcome! </body></html>" % name
    return HttpResponse(html)