from django.db import models
from django.conf import settings

# class Post(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     image = models.ImageField(upload_to='posts/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.title
#
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Comment by {self.user} on {self.post.title}"

from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError





def validate_image_size(image):
    max_size = 11 * 1024 * 1024  # 5MB in bytes
    if image.size > max_size:
        raise ValidationError("The image size must not exceed 10 MB.")

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to='posts/', blank=False, null=False, validators=[validate_image_size])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
