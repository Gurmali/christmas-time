from django.contrib import admin
from .models import Post, Comments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'poster', 'slug', 'created_on')
    search_fields = ['title', 'poster__username', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('poster__username', 'created_on')
    summernote_fields = ('content')


@admin.register(Comments)
class CommentsAdmin(SummernoteModelAdmin):

    list_display = ('__str__', 'poster', 'comment', 'post', 'created_on')
    list_filter = ('poster', 'created_on')
    search_fields = ('poster__username', 'comment')
    summernote_fields = ('comment')
