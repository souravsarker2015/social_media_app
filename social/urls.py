from django.urls import path
from social import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='post_details'),
    path('post/edit/<int:pk>/', views.PostEditView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', views.CommentsDeleteView.as_view(), name='comment_delete'),
]
