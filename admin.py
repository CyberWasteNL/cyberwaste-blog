from django.db import models
from django.contrib import admin
from epiceditor.widgets import AdminEpicEditorWidget

from models import Article, Category


class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created', 'category')
    formfield_overrides = {
        models.TextField: {'widget': AdminEpicEditorWidget},
    }


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Category)