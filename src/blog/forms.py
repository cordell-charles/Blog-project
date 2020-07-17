from django import forms
from .models import BlogPost



class BlogPostForm(forms.ModelForm):

	title 	= forms.CharField()
	content = forms.CharField(widget= forms.Textarea)

	class Meta:
		model = BlogPost
		fields = ['title','slug','content']