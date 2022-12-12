from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from sonishop.models import Article
from sonishop.api.serializers import ArticleSerializer

from django.contrib.auth.models import User

@api_view(['GET', ])
def api_show_article(request, id):
    try:
        article = Article.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

@api_view(['GET', ])
def api_articles(request):
    articles = Article.objects.all()
    
    if request.method=="GET":
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

@api_view(['PUT', ])
def api_update(request, id):
    try:
        article = Article.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="PUT":
        serializer = ArticleSerializer(article, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['sucess'] = "update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE', ])
def api_delete(request, id):
    try:
        article = Article.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=="DELETE":
        operation = article.delete()
        data = {}
        if operation:
            data['sucess'] = "deleted successful"
        else:
            data['failure'] = "delete failed"
        return Response(data=data)


@api_view(['POST', ])
def api_create_article(request):
    author = User.objects.get(pk=1)
    article = Article(author=author)
    if request.method=="POST":
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)