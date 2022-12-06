from django.contrib import admin
from .models import Photo, PhotoAdmin
from .models import Article, ArticleAdmin

# Register your models here.
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Article, ArticleAdmin)
