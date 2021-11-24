from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=150)
    body = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # author = models.CharField(max_length=150, default="Admin")
    
    def publish(self):
        self.published_date = timezone.now()
        self.save
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "-published_date",
        ]
