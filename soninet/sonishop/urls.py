from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('article/<int:id>', views.show, name="show"),
    path('article', views.create_article, name="article"),
    path('article/<int:id>/edit', views.edit, name="edit"),
]