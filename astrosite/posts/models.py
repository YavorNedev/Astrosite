
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError





def validate_image_size(image):
    max_size = 10 * 1024 * 1024
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
