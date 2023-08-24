from django.contrib import admin

from blog.models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'category', 'tag', 'image', 'image_text', 'preview_text', 'main_text']
    list_display = ['title', 'category']
    prepopulated_fields = {'slug': ('title', )}
