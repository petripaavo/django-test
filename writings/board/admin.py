from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at', 'parent')
    search_fields = ('text', 'author')
    list_filter = ('created_at',)