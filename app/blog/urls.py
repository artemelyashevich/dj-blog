from django.urls import path
from . import views


urlpatterns = [
    path("", views.PostHome.as_view(), name="home"),
    path("post/<int:post_id>/", views.PostPage.as_view(), name="post"),
    path("add-post/", views.PostAdd.as_view(), name="add_post"),
    path("category/<str:cat>", views.PostCategory.as_view(), name="category"),
    path("register/", views.UserRegister.as_view(), name="register"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("logout", views.user_logout, name='logout'),
]
