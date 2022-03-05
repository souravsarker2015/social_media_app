from django.contrib import admin
from .models import Post, Comments, UserProfile, Notification, MessageModel, Tag, Image, ThreadModel


# from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'body', 'created_on', 'author']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'comment', 'post', 'created_on', 'author']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'bio', 'birth_date', 'location', 'picture']


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'notification_type', 'to_user', 'from_user', 'post', 'comment', 'date', 'user_has_seen']


@admin.register(ThreadModel)
class ThreadModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'receiver']


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'thread', 'sender_user', 'receiver_user', 'body', 'image', 'date', 'is_read']


@admin.register(Image)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
