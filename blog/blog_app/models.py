from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 264)
    author = models.ForeignKey(User)
    text = models.TextField(null=True)
    created_date = models.DateField(default = timezone.now)
    published_date = models.DateField(blank = True,null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_app:post_detail", kwargs = {'pk' : self.pk})

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment = True) 


class Comment(models.Model):
    post = models.ForeignKey(Post , related_name="comments")
    commenter = models.CharField(max_length = 264)
    comment = models.TextField()
    created_date = models.DateField(default = timezone.now)
    approved_comment = models.BooleanField(default = False)

    def __str__(self):
        return self.comment

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("blog_app:post_list")
    