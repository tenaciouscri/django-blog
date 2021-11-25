from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog, Comment

# Register your models here.


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = "body"
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment)


class BlogAdminArea(admin.AdminSite):
    site_header = "Blog Admin Area"
    login_template = "blog/admin/login.html"


blog_site = BlogAdminArea(name="BlogAdmin")


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"
