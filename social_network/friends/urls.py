from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.FriendListView.as_view(), name='friend_list'),
]