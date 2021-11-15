import git
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.utils import timezone
from django.shortcuts import redirect

from .models import Blog
from .models import Post

from .forms import PostForm


# MY OWN DEF


def home(request):
    blog_posts = Blog.objects.all()
    posts = Post.objects.all()
    context = {"blog_posts": blog_posts, "posts": posts}
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
            post.date = timezone.now()
            post.save()
            return redirect('blog_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post(request, id=1):
    post = Post.objects.get(id=id)
    context = {"post": post}
    return render(request, "blog/post.html", context)


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
