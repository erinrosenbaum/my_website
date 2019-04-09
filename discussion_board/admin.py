from django.contrib import admin

from . import models

class CommentInline(admin.TabularInline):
    model = models.Comment

class DiscussionAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(models.Discussion, DiscussionAdmin)
admin.site.register(models.Comment)
