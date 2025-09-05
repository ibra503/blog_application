# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class blog(models.Model):
    title = models.CharField()
    body = models.TextField()

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class Comment(models.Model):
    post = models.ForeignKey("Post", related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)











