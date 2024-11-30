from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'created_at', 'updated_at', 'image_preview')



    list_filter = ('author', 'created_at', 'updated_at')


    search_fields = ('title', 'content')


    readonly_fields = ('created_at', 'updated_at', 'image_preview')


    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image', 'image_preview', 'author')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
        }),
    )


    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" style="width: 100px; height: auto;">')
        return "No Image"
    image_preview.short_description = "Image Preview"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('author', 'post', 'content', 'created_at')


    list_filter = ('post', 'created_at')


    search_fields = ('content', 'author__username')


    readonly_fields = ('created_at',)

