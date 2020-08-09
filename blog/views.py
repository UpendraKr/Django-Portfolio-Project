from django.shortcuts import render, get_object_or_404
from blog.models import Blog


def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blog.html', {'blogs': blogs})


def detail(request, blog_id):
    detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detail': detail})