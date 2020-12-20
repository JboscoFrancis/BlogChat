from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)    #when user is deleted post is deleted too
    title = models.CharField(max_length=100, null=True)
    date_created = models.DateField(auto_now_add=True,)
    post = models.TextField(null=True)

    def __str__(self):
        return self.title

class Reply(models.Model):
    reply_post = models.ForeignKey(Post, null=True, on_delete=models.CASCADE)       #when Post is deleted reply is deleted too
    reply_user = models.CharField(max_length=100, null=True)
    reply_date = models.DateTimeField(auto_now_add=True)
    reply_comment = models.TextField(max_length=500, null=True)

    def __str__(self):
        return self.reply_comment

class Profile(models.Model):
    user = models.OneToOneField(User, null =True, blank=True, on_delete=models.CASCADE) #when user is deleted profile is deleted too
    profile = models.ImageField(null=True, )
    
