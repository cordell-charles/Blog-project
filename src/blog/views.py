from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm



@login_required
def blog_post_list_view(request):
	# List out objects - also search functionality
	qs = BlogPost.objects.all()
	template_name = 'blog/list.html'
	context = {'object_list': qs}
	return render(request, template_name, context)


@login_required
def blog_post_create_view(request):
	# Create new blog objects 
	template_name = 'blog/create.html'
	form = BlogPostForm(request.POST or None)
	if form.is_valid():
		obj = form.save(commit= False)
		obj.user = request.user
		obj.save()
		form = BlogPostForm()
	context = {'form': form }
	return render(request, template_name, context)

@login_required
def blog_post_retrieve_view(request, slug):
	# Detail view - for single objects 
	template_name = 'blog/detail.html'
	obj = get_object_or_404(BlogPost, slug=slug)
	context = {"object": obj}
	return render(request, template_name, context)

@login_required
def blog_post_update_view(request, slug):
	template_name = 'blog/create.html'
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	context = {'form': form, "title": f"Update {obj.title}"}
	return render(request, template_name, context)

@login_required
def blog_post_delete_view(request, slug):
	template_name = 'blog/delete.html'
	obj = get_object_or_404(BlogPost, slug=slug)
	if request.method == "POST":
		obj.delete()
		return redirect("/blog")
	context = {"object": obj}
	return render(request, template_name, context)


