from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('date_create',)
    list_display = ('pk','title', 'text', 'date_create', 'published', 'views_count')
    list_filter = ('published', 'views_count')
    search_fields = ('text', 'title')
