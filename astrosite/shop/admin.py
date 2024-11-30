from django.utils.html import format_html
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'image_preview', 'stock', 'created_at', 'updated_at')
    list_filter = ('category', 'price')
    search_fields = ('name', 'description', 'stock')
    list_editable = ('price', 'stock')

    readonly_fields = ('image_preview',)

    def image_preview(self, obj):

        if obj.image:
            return format_html('<img src="{}" style="max-width: 100px; max-height: 100px;" />', obj.image.url)
        return "No image"

    image_preview.short_description = 'Image Preview'





