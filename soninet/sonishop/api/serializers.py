from rest_framework import serializers
from sonishop.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['author', 'title', 'details', 'price']