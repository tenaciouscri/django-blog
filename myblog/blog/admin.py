from django.contrib import admin
from . import models
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog
from .models import Post

# Register your models here.


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = "body"
    pass


admin.site.register(Blog, BlogAdmin)


class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    login_template = "blog/admin/login.html"


blog_site = BlogAdminArea(name="BlogAdmin")


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"


admin.site.register(models.Post, SummerAdmin)
blog_site.register(models.Post, SummerAdmin)
