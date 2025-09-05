from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class blogs(models.Model):
    title = models.CharField(max_lenght=200)
    body = models.TextField()

class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)











