from django.urls import path
from .views import article_func, article_detail, article_create, article_edit, article_delete, like_article, dislike_article, comment_delete, comment_edit

urlpatterns = [
    path('', article_func, name='article_func'),
    path('<slug>',article_detail, name="article_detail"),
    path('create/', article_create, name='article_create'),
    path('<slug>/edit', article_edit, name='article_edit'),
    path('<slug>/delete', article_delete, name='article_delete'),

    path('<slug>/like', like_article, name='article_like'), 
    path('<slug>/dislike', dislike_article, name='article_dislike'),

    path('<slug>/delete/<int:pk>', comment_delete, name='comment_delete'),
    path('<slug>/edit/<int:pk>', comment_edit, name='comment_edit')
]