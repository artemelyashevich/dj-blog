from django.shortcuts import render, redirect

from .forms import AddPostForm
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


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except Exception as e:
                print(e)
                form.add_error(None, 'Ошибка!!!')
    else:
        form = AddPostForm()
    return render(request, 'blog/add-post.html', {'navs': menu, 'title': 'Добавить статью', 'form': form})
