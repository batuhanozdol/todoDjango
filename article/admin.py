from django.contrib import admin
from .models import Article
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","date"]
    liste_display_links = ["title","date"]
    
    search_fields = ["title"]
    list_filter = ["date"]
    class Meta:
        model = Article