from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import AddPostForm
from .models import Post

menu = [
    {'title': 'Главная', 'path': '/'},
    {'title': 'Добавить статью', 'path': '/add-post'},
    {'title': 'Войти', 'path': '/login'},
]

category_list = [
    {'title': 'Люди', 'path': 'man'},
    {'title': 'Электроника', 'path': 'el'},
    {'title': 'Книги', 'path': 'book'}
]


class PostHome(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['navs'] = menu
        context['title'] = 'Главная'
        context['cats'] = category_list
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostCategory(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str('Категория ' + str(context['posts'][0].category))
        context['navs'] = menu
        context['cat_selected'] = self.kwargs['cat']
        context['cats'] = category_list
        return context

    def get_queryset(self):
        return Post.objects.filter(category=self.kwargs['cat'].upper(), is_published=True)


class PostPage(DetailView):
    model = Post
    template_name = 'blog/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пост'
        context['navs'] = menu
        context['cats'] = category_list
        return context


class PostAdd(CreateView):
    form_class = AddPostForm
    template_name = 'blog/add-post.html'
    success_url = reverse_lazy('/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['navs'] = menu
        context['cats'] = category_list
        return context