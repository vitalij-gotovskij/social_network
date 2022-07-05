from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")


class PostListView(generic.ListView):
    model = Post
    template_name = 'post_list.html'
    

class PostCreateView(LoginRequiredMixin, generic.CreateView): 
    model = Post
    fields = ['owner', 'content', 'pin_to_top']
    success_url = "/posts/list"
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
