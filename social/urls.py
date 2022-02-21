from django.urls import path
from social import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='post_details'),
    path('post/edit/<int:pk>/', views.PostEditView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),

    path('post/<int:post_pk>/comment/delete/<int:pk>/', views.CommentsDeleteView.as_view(), name='comment_delete'),
    path('post/<int:post_pk>/comment/<int:pk>/like/', views.AddCommentLike.as_view(), name='comment-like'),
    path('post/<int:post_pk>/comment/<int:pk>/dislike/', views.AddCommentDislike.as_view(), name='comment-dislike'),

    path('post/<int:post_pk>/comment/<int:pk>/reply/', views.CommentReplyView.as_view(), name='comment-reply'),

    path('post/<int:pk>/like/', views.AddLikes.as_view(), name='like'),
    path('post/<int:pk>/dislike/', views.AddDislike.as_view(), name='dislike'),

    path('profile/<int:pk>/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', views.ProfileEditView.as_view(), name='profile_edit'),

    path('profile/<int:pk>/followers', views.ListFollowers.as_view(), name='list-followers'),
    path('profile/<int:pk>/follower/add/', views.AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/follower/remove/', views.RemoveFollower.as_view(), name='remove-follower'),
    path('search/', views.UserSearch.as_view(), name='profile-search'),
    path('search/', views.UserSearch.as_view(), name='profile-search'),
]
