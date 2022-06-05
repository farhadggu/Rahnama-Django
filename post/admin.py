from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('دسته بندی مادر / فرزند', {'fields': ('parent', 'is_sub', 'title_fa', 'title_en', 'slug')}),
        ('در صورتی که این دسته بندی شامل توضیحات میباشد این بخش پر شود',
            {'fields': ('title_post_fa', 'title_post_en', 'desc_post_fa', 'desc_post_en', 'img_post', 'video_post', 'file')}
        ),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)