from django.contrib import admin
from .models import *
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'date_publish', 'is_recommend')
    filter_horizontal = ('tag',)
    search_fields = ('title',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Category)
