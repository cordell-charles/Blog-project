from django.http import HttpResponse
from django.shortcuts import render
from .form import ContactForm



def home_page(request):
	return render(request, "base.html")


def about(request):
	return HttpResponse("about page/cv page")

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form = ContactForm()
	context = {
		"title":"contact us", 
		"form": form
	}
	return render(request, "contact.html", context)
