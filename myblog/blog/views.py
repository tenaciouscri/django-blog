from django.contrib.auth import login
import git
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.utils import timezone
from django.shortcuts import redirect

from .models import Blog, Comment

from .forms import CommentForm, PostForm

from django.contrib.auth.decorators import login_required


# MY OWN DEF


def home(request):
    blog_posts = Blog.objects.filter(published_date__lte=timezone.now()).order_by(
        "-published_date"
    )
    return render(request, "blog/home.html", {"blog_posts": blog_posts})


def blog_post(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, "blog/blog_post.html", {"blog": blog})


def add_comment(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            return redirect("blog_post", pk=blog.pk)
    else:
        form = CommentForm()
    return render(request, "blog/add_comment.html", {"form": form})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog_post", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog_post", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_edit.html", {"form": form})


@login_required
def post_draft_list(request):
    blog_posts = Blog.objects.filter(published_date__isnull=True).order_by(
        "-created_date"
    )
    return render(request, "blog/post_draft_list.html", {"blog_posts": blog_posts})


@login_required
def post_publish(request, pk):
    blog_post = get_object_or_404(Blog, pk=pk)
    blog_post.publish()
    return redirect("blog_post", pk=pk)


@login_required
def post_remove(request, pk):
    blog_post = get_object_or_404(Blog, pk=pk)
    blog_post.delete()
    return redirect("home")


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect("blog_post", pk=comment.blog.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect("blog_post", pk=comment.blog.pk)


# DEF FOR AUTO PULL FROM PYTHONANYWHERE


@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo("django-blog/")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
