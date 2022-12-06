from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to="media/img")

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['photo']

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    details = models.TextField(max_length=100)
    price = models.FloatField()
    images = models.ManyToManyField("photo", blank=True)
    creat_at = models.DateTimeField(auto_now=True)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'details', 'price', 'creat_at']