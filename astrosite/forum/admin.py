from django.contrib import admin
from .models import Thread

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)


    readonly_fields = ('created_at',)
