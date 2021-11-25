import git
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.utils import timezone
from django.shortcuts import redirect

from .models import Blog

from .forms import PostForm


# MY OWN DEF


def home(request):
    blog_posts = Blog.objects.all()
    context = {"blog_posts": blog_posts}
    return render(request, "blog/home.html", context)


def blog_post(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_post.html', {'blog': blog})
    # blog = Blog.objects.get(id=id)
    # context = {"blog": blog}
    # return render(request, "blog/blog_post.html", context)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect('blog_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_draft_list(request):
    posts = Blog.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

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
