from django.shortcuts import render, redirect
from . models import Photo, Article
from .forms import PhotoForm, ArticleForm
from django.contrib.auth.models import User

def index(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, "sonishop/index.html", context)

def show(request, id):
    article = Article.objects.get(pk=id)
    if request.method=="POST":
        new_photo = Photo()
        new_photo.author = User.objects.get(pk=request.user.id)
        new_photo.photo = request.FILES['photo']
        new_photo.save()
        
        article.images.add(new_photo)
    
    form = PhotoForm()
    context = {'article' : article, 'form': form}
    return render(request, "sonishop/show.html", context)

def create_article(request):
    if request.method=="POST":
        new_article = Article()
        new_article.author = User.objects.get(pk=request.user.id)
        new_article.title = request.POST["title"]
        new_article.details = request.POST["details"]
        new_article.price = request.POST["price"]
        new_article.save()
        return redirect(f"/article/{new_article.id}")

    form = ArticleForm()
    context = {'form' : form}
    return render(request, "sonishop/new_article.html", context)

def edit(request, id):
    article = Article.objects.get(pk=id)
    context = {'article' : article}
    if request.method=="POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(f'/article/{article.id}')


    context['form'] = ArticleForm(instance=article)
    return render(request, "sonishop/edit.html", context)
