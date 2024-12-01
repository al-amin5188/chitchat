from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    picture = models.ImageField(upload_to='post_images/', blank=True, null=True)
    video = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    related_post = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    # ManyToManyField for likes and saves so users can interact with multiple posts
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    saves = models.ManyToManyField(User, related_name='saved_posts', blank=True)

    def total_likes(self):
        return self.likes.count()

    def total_comments(self):
        return self.comments.count()  # Related name used in Comment model

    def total_saves(self):
        return self.saves.count()
    
    def __str__(self):
        return self.content[:30] if self.content else "No Content"

    class Meta:
        # Unique constraint on the combination of user and post for likes and saves
        constraints = [
            models.UniqueConstraint(fields=['user', 'likes'], name='unique_like_post'),
            models.UniqueConstraint(fields=['user', 'saves'], name='unique_save_post')
        ]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    picture = models.ImageField(upload_to='comment_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    
    def total_likes(self):
        return self.likes.count()
    
    def total_replies(self):
        return self.replies.count()

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}"

    class Meta:
        # Unique constraint to ensure a user can like only once per comment
        constraints = [
            models.UniqueConstraint(fields=['user', 'comment'], name='unique_like_comment')
        ]
