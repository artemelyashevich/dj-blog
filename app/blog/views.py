from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import AddPostForm, UserRegisterForm, UserLoginForm
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


class UserRegister(DataMixin, CreateView):
    form_class = UserRegisterForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class UserLogin(DataMixin, LoginView):
    form_class = UserLoginForm
    template_name = 'blog/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c = self.get_user_context(title='Вход')
        return dict(list(context.items()) + list(c.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def user_logout(request):
    logout(request)
    return redirect('login')
