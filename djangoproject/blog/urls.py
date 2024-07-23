from django.contrib import admin
from django.urls import path
from . import views
from  .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView
#code

urlpatterns = [
    path('',PostListView.as_view(),name='blog-home' ),
    path('about/',views.About.as_view(),name='blog-about' ),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='update-view'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'), 
    path('user/<str:username>/',UserPostListView.as_view(),name='user-posts'), 
]