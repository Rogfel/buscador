from django.conf.urls.defaults import *
from piston.resource import Resource
from api.piston.handlers import *


article_handler = Resource(ArticleHandler)
buscar_handler = Resource(BuscarHandler)

urlpatterns = patterns('',
   url(r'^article/(?P<id>[^/]+)/', article_handler),
   url(r'^article/$', article_handler),
   url(r'^buscar/$', article_handler),
)
