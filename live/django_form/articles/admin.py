from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at', 'updated_at', )

admin.site.register(Article, ArticleAdmin) # 어드민 사이트에 등록해줘(특정한 모델을)
