import uuid

from django.db import models
from django.contrib.auth.models import User
from tinymce import models as tinymce_models
from django.urls import reverse


class Wall(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)
    pin_to_top = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = tinymce_models.HTMLField(default='')
    wall = models.ForeignKey('Wall', on_delete=models.SET_NULL, null=True)
    pin_to_top = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    reply_to = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, blank=True, related_name="replies")
    repost_of = models.ForeignKey('Post', on_delete=models.SET_NULL, null=True, blank=True, related_name="reposts")

    def __str__(self):
        return f"{self.owner} - {self.content}"
    
    def get_absolute_url(self):
        return reverse('post-list', args=[str(self.id)])


class Meta:
    verbose_name = 'Post'
    verbose_name_plural = 'Posts'


class Like(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for every like')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text='Time of like')

    def __str__(self):
        return self.id