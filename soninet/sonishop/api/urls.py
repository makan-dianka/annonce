from django.urls import path
from sonishop.api import views

app_name = 'soninet'
urlpatterns = [
    path('article/<int:id>', views.api_show_article, name="article_show"),
    path('article/<int:id>/edit', views.api_update, name="article_edit"),
    path('article/<int:id>/delete', views.api_delete, name="article_delete"),
    path('article/create', views.api_create_article, name="article_create"),
    path('articles', views.api_articles, name="articles"),
]