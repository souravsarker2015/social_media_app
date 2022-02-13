from django.urls import path
from social import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetails.as_view(), name='post_details'),
]
