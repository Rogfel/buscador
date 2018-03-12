from django.contrib import admin
from comment_sample.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display=('id','name')
    search_fields = ['name']
    
admin.site.register(Article, ArticleAdmin)