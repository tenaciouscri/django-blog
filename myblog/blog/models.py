from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=150, default = "Admin")
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date',]

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(default=None, blank=True)
    author = models.CharField(max_length=150, default = "Admin")
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date',]