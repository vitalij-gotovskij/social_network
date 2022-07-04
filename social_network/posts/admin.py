from django.contrib import admin
from .models import Wall, Post, Like

# Register your models here.


admin.site.register(Wall)
admin.site.register(Post)
admin.site.register(Like)