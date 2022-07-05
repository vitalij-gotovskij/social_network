from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Friend

class FriendListView(generic.ListView):
    model = Friend
    template_name = 'friend_list.html'