from django.db import models
from django.contrib import admin
import random


class myBlog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    name = str(random.randint(12, 24))


class blogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')

# class Meta:
    # ordering =('-timestamp')
admin.site.register(myBlog, blogPostAdmin)
