import git
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render
from django.http import HttpResponse

from .models import Blog
from .models import Post

# DEF FOR AUTO PULL FROM PYTHONANYWHERE

@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be 
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("tenaciouscri.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

# MY OWN DEF

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