from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Reply, Profile


# here i created model based form

#Post creation form
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post',)


#user registration form
class UserRegistration(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


#post comment_reply form
class ReplyForm(ModelForm):
    class Meta:
        model = Reply
        fields = ('reply_user','reply_comment',)

#update profile info form
class UpdateProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

#change profile picture form
class UpdatePicture(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile',)
