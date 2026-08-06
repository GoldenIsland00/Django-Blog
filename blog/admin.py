from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Category, Tag, Post, Comment, Profile


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'slug', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(TranslationAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'views_count', 'published_at')
    list_filter = ('status', 'is_featured', 'category', 'created_at', 'published_at')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published_at'
    filter_horizontal = ('tags',)
    list_editable = ('status', 'is_featured')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'author', 'category', 'tags')
        }),
        ('Content', {
            'fields': ('cover_image', 'excerpt', 'content')
        }),
        ('Publishing', {
            'fields': ('status', 'is_featured', 'published_at')
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('content', 'author__username')
    list_editable = ('is_approved',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'created_at')
    search_fields = ('user__username', 'bio')
