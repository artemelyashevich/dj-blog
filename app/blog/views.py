from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .forms import AddPostForm
from .models import Post
from .utils import DataMixin


class PostHome(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.get_user_context(title='Главная')
        return dict(list(context.items()) + list(c.items()))

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostPage(DataMixin, DetailView):
    model = Post
    template_name = 'blog/post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.get_user_context(title='Статья')
        return dict(list(context.items()) + list(c.items()))


class PostCategory(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.get_user_context(title='Категория ' + str(context['posts'][0].category),
                                  cat_selected=self.kwargs['cat'])
        return dict(list(context.items()) + list(c.items()))

    def get_queryset(self):
        return Post.objects.filter(category=self.kwargs['cat'].upper(), is_published=True)


class PostAdd(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/add-post.html'
    login_url = '/admin/'
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c.items()))
