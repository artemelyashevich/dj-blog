from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'photo', 'time_create', 'time_update')
    list_display_links = ('id', 'title')
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
