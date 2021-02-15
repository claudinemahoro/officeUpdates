from django import forms
from .models import Profile, Post

class NewPostForm(forms.ModelForm):
  class Meta:
    model = Post
    exclude = ['post_date']

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']
