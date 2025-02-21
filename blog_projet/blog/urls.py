from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('create/', views.create_post, name='create_post'),
    path('blog', views.blog, name='blog'),
]