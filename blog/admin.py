from django.contrib import admin

from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    search_fields = ("title", )
    prepopulated_fields = {"slug": ("title", )}


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "time_created", "time_updated")
    search_fields = ("title", )
    list_filter = ("time_created", )
    readonly_fields = ("time_created", "time_updated")
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
