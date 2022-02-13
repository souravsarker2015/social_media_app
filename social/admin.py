from django.contrib import admin
from .models import Post, Comments, UserProfile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'body', 'created_on', 'author']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'created_on', 'author']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'bio', 'birth_date', 'location', 'picture']
