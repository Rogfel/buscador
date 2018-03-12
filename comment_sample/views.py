from comment_sample.models import *
from django.http import * 
from django.template import RequestContext, loader
from comment_sample.form import BuscarForm
from motor.search_django import Search
from django.views.decorators.csrf import csrf_protect
from django.utils import simplejson

def getResponse(request,template,context):
    t = loader.get_template(template)
    c = RequestContext(request, context)
    return HttpResponse(t.render(c))

def index(request):
    articles= Article.objects.all()
    return getResponse(request,'index.html', 
                       {'articles': articles})
    
def article_detail(request,id):
    ''''this will show the details of an article
    Since we are interested in only implementing the comment framework
    I'm not going to give a thorough checking below'''
    article= Article.objects.get(id=id)
    return getResponse(request, 'detail.html', 
                       {'article':article})


@csrf_protect
def busqueda(request):
    data = {'ok':'f'}
    if request.method == 'GET':
        GET = request.GET
        if GET.has_key('buscar'):
            bus = Search()
            result = bus.search(GET['buscar'])
            data = {'ok':'t','result':result}
    json = simplejson.dumps(data)
    return HttpResponse(json, mimetype='application/json')      
    return HttpResponse(json, mimetype='application/json')