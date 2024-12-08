# from django.contrib import admin
# from .models import Thread
#
# @admin.register(Thread)
# class ThreadAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user', 'created_at')
#     list_filter = ('created_at', 'user')
#     search_fields = ('title', 'content')
#     ordering = ('-created_at',)
#
#
#     readonly_fields = ('created_at',)

from django.contrib import admin
from .models import Category, Thread, Comments

# Register the Categorys model in the admin interface
@admin.register(Category)
class CategorysAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Display these fields in the admin list view
    search_fields = ('name', 'description')  # Add a search box for these fields

# Register the Thread model in the admin interface
@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')  # Display these fields in the admin list view
    list_filter = ('created_at', 'user')  # Add filters for these fields
    search_fields = ('title', 'content')  # Add a search box for these fields
    ordering = ('-created_at',)  # Order threads by creation date descending
    readonly_fields = ('created_at',)  # Make the created_at field read-only

# Register the Comments model in the admin interface
@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('thread', 'author', 'content', 'created_at')  # Display these fields in the admin list view
    list_filter = ('created_at', 'author')  # Add filters for these fields
    search_fields = ('content', 'author__username')  # Add a search box for these fields