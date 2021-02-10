from django import forms
from .models import Profile, Post

class NewPostForm(forms.Form):
  class Meta:
    model = Post
    exclude = ['post_user','post_department']

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']