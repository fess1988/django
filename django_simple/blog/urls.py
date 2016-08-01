from django.conf.urls import *
from django_simple.blog.views import archive

urlpatterns = patterns('', url(r"^$", archive)
)