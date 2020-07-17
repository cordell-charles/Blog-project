from django import forms

class ContactForm(forms.Form):
	first_name = forms.CharField()
	last_name  = forms.CharField()
	email	   = forms.EmailField()
	content    = forms.CharField(widget= forms.Textarea)