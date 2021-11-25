from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page="/"), name="logout"),
    path("", views.home, name="home"),
    path('blog/<int:pk>/', views.blog_post, name='blog_post'),
    path('blog/new/', views.post_new, name='post_new'),
    path('blog/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('blog/<pk>/publish/', views.post_publish, name="post_publish"),
    path('blog/<pk>/remove/', views.post_remove, name="post_remove"),
    path("summernote/", include("django_summernote.urls")),
    path("update_server/", views.update, name="update"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )  # sets static files and the media root
    