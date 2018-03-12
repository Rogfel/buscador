from django.conf.urls.defaults import patterns, include, url
from comment_sample.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #basic app with 1 model and displaying the model
    url(r'^$', index, name='home'),
    url(r'^article-(?P<id>\d+)$', article_detail, name='article_detail'),
    url(r'^admin/', include(admin.site.urls)),
    
    #comments framework
    (r'^comments/', include('django.contrib.comments.urls')),
     
    # piston framework
    url(r'^api/piston/', include('api.piston.urls')),
	
	# buscar
    url(r'^buscar$',busqueda, name='busqueda')
)
