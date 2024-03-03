from django.contrib import admin
from .models import Articles, Comments


admin.site.register(Articles)


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'post')
