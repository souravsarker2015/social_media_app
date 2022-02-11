from django.urls import path
from social import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts'),
]
