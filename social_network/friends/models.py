from django.conf import settings
from django.db import models
# from django.utils.translation import gettext_lazy as _


# Create your models here.
from tinymce.models import HTMLField


class Friend(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="user",
        on_delete=models.CASCADE,
        related_name='friend_requests',
    )
    friend = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="friend",
        on_delete=models.CASCADE,
        related_name='friends',
    )
    is_accepted = models.BooleanField("accepted", default=False)
    is_blocked = models.BooleanField("blocked", default=False)
    request_message = HTMLField("request message", blank=True, null=True)
    created_at = models.DateTimeField("created at", auto_now_add=True)
    updated_at = models.DateTimeField("updated_at", auto_now=True)