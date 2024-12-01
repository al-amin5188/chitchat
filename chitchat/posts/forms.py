from django import forms
from .models import Post, Comment, Rating

# পোস্ট তৈরি করার জন্য ফর্ম
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

# মন্তব্য তৈরি করার জন্য ফর্ম
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# রেটিং তৈরি করার জন্য ফর্ম
class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
