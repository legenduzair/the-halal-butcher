from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost


class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(BlogPost, PostAdmin)
