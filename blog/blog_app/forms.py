from django import forms
from blog_app.models import Post,Comment

class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post
        fields = ("title","author","text")

        widget = {
            'title': forms.TextInput(attrs = {'class':'post_form_title'}),
            'text' : forms.Textarea(attrs = {'class':'editable medium-editor-textarea text_area_class'})
        }

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("commenter","comment")

        widget = {
            'comment' : forms.Textarea(attrs = {'class':'editable medium-editor-textarea textarea_class'})
        }
