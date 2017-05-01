from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		widgets = {
          'content': forms.Textarea(attrs={'rows':20, 'cols':100}),
        }
		fields = ['title', 'content']
