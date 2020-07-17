from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm



def blog_post_list_view(request):
	# List out objects - also search functionality
	qs = BlogPost.objects.all()
	template_name = 'blog/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)


def blog_post_create_view(request):
	# Create new blog objects 
	template_name = 'blog/create.html'
	form = BlogPostForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = BlogPostForm()
	context = {'form': form }
	return render(request, template_name, context)

def blog_post_retrieve_view(request, slug):
	# Detail view - for single objects 
	template_name = 'blog/detail.html'
	obj = get_object_or_404(BlogPost, slug=slug)
	context = {"object": obj}
	return render(request, template_name, context)

def blog_post_update_view(request, slug):
	template_name = 'blog/update.html'
	obj = get_object_or_404(BlogPost, slug=slug)
	context = {"object": obj, 'form': None}
	return render(request, template_name, context)

def blog_post_delete_view(request, slug):
	template_name = 'blog/delete.html'
	obj = get_object_or_404(BlogPost, slug=slug)
	context = {"object": obj}
	return render(request, template_name, context)


