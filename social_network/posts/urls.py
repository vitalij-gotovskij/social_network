from django.urls import path
from .views import index, PostCreateView, PostListView, PostDetailView

urlpatterns = [
    path('', index, name='index'),
    path('list/', PostListView.as_view(), name='post_list'),
    path('list/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view(), name='create-post'),
]