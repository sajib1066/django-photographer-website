from django.contrib import admin
from .models import Category, Gallery

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_delete', 'author', 'date']
    list_filter = ['name', 'is_delete', 'author']
    search_fields = ['name']

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_delete', 'author', 'date']
    list_filter = ['title', 'category', 'is_delete', 'author']
    search_fields = ['title']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Gallery, GalleryAdmin)
