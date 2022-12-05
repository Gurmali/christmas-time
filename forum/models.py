from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Post(models.Model):
    '''postmodel'''
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    poster = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    poster = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments")
    comment = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name="comment_likes", blank=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.poster} says: {self.comment}"

    def number_of_likes(self):
        return self.likes.count()
