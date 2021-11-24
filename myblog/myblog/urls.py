from django.contrib import admin
from django.urls import path
from django.urls import include
from blog import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path('blog/<int:pk>/', views.blog_post, name='blog_post'),
    path('blog/new/', views.post_new, name='post_new'),
    path('blog/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # path("blog/<int:id>/", views.blog_post, name="blog_post"),
    # path('post/<int:id>/', views.post, name="post"),
    path("summernote/", include("django_summernote.urls")),
    path("update_server/", views.update, name="update"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )  # sets static files and the media root
