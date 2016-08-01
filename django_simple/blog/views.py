from django.http import HttpResponse
from django.template import loader, Context
from django_simple.blog.models import myBlog


def archive(request):
    posts = myBlog.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))