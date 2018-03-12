from comment_sample.models import *
from piston.handler import BaseHandler
from motor.search_django import Search

class CsrfExemptBaseHandler(BaseHandler):
    """
    handles request that have had csrfmiddlewaretoken inserted 
    automatically by django's CsrfViewMiddleware
    taken from: http://andrew.io/weblog/2010/01/django-piston-and-handling-csrf-tokens/
    """
    def flatten_dict(self, dct):
        if 'csrfmiddlewaretoken' in dct:
            # dct is a QueryDict and immutable
            dct = dct.copy()  
            del dct['csrfmiddlewaretoken']
        return super(CsrfExemptBaseHandler, self).flatten_dict(dct)

class ArticleHandler(CsrfExemptBaseHandler):
    allowed_methods = ('GET',)
    model = Article 
    fields = ('id', 'name', 'value', 'status_text')

    def read(self, request, id=None, start_id = None):
        ''' handle GET requests'''
        if id:
            return Article.objects.get(id=id)
        else:
            return Article.objects.all()
    
    @classmethod
    def status_text(self, obj):
        return Article.STATUS_TYPES[obj.status][1]

class BuscarHandler(CsrfExemptBaseHandler):
    allowed_methods = ('POST',)
    #model = Article
    bus = Search()
    fields = ('id', 'name', 'value')

    def create(self, request, id=None, start_id = None):
        ''' handle POST requests'''
        attrs = self.flatten_dict(request.POST)
        if attrs.has_key('buscar'):
            return bus.search(request.POST.get('buscar'))
        else:
            return bus.search('rogfel apple')

    @classmethod
    def status_text(self, obj):
        return Article.STATUS_TYPES[obj.status][1]