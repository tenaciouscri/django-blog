"""myblog URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.home, name="home"),
    path('blog/<int:pk>/', views.blog_post, name='blog_post'),
    path('blog/new/', views.post_new, name='post_new'),
    # path("blog/<int:id>/", views.blog_post, name="blog_post"),
    # path('post/<int:id>/', views.post, name="post"),
    path("admin/", admin.site.urls),
    path("summernote/", include("django_summernote.urls")),
    path("update_server/", views.update, name="update"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )  # sets static files and the media root
