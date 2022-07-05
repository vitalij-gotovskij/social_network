from django.urls import path
from .views import PostCreateView, PostListView, index

urlpatterns = [
    path('', index, name='index'),
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('create_post/', PostCreateView.as_view(), name='create-post'),
]