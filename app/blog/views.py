from django.http import HttpResponse
from django.shortcuts import render

from .models import Post

menu = [
    {
        'title': 'Главная', 'path': '/'}, {'title': 'Добавить статью', 'path': '/add-post'},
    {'title': 'Войти', 'path': '/login'}]


def index(request):
    posts = Post.objects.all()

    return render(request, 'blog/index.html', {'navs': menu, 'posts': posts, 'title': 'home'})


def post(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    return render(request, 'blog/post.html', {"post": post, "navs": menu})
