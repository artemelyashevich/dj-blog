from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Post


class AddPostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = False

    class Meta:
        model = Post
        fields = ['title', 'content', 'photo', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__title'}),
            'content': forms.Textarea(attrs={'class': 'form__content'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов!')
        return title


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__title'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form__title'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form__title'}))

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2'}
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form__title'}),
            'password1': forms.PasswordInput(attrs={'class': 'form__title'}),
            'password2': forms.PasswordInput(attrs={'class': 'form__title'}),
        }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__title'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__title'}))
