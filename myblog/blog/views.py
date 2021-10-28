from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog
from .models import Post


def home(request):
    blog_posts = Blog.objects.all()
    posts = Post.objects.all()
    context = {"blog_posts": blog_posts, "posts": posts}
    return render(request, "blog/home.html", context)


def blog_post(request, id=1):
    blog = Blog.objects.get(id=id)
    context = {"blog": blog}
    return render(request, "blog/blog_post.html", context)


def post(request, id=1):
    post = Post.objects.get(id=id)
    context = {"post": post}
    return render(request, "blog/post.html", context)