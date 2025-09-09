from django.db import models
from django.contrib.auth.models import User

from django.conf import settings

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add extra fields if you want
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)