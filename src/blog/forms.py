from django import forms
from .models import BlogPost
from django.forms import ValidationError



class BlogPostForm(forms.ModelForm):

	content = forms.CharField(widget= forms.Textarea)


	class Meta:
		model = BlogPost
		fields = ['title','slug','content', 'image', 'publish_date']

	def clean_title(self, *args, **kwargs):
		instance = self.instance
		title = self.cleaned_data.get('title')
		qs = BlogPost.objects.filter(title__iexact= title)
		if instance is not None:
			qs = qs.exclude(pk=instance.pk)
		if qs.exists():
			raise ValidationError("This title has already been used by you, please try a different name")
		return title
