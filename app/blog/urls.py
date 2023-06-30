from django.urls import path

from .views import index, post, add_post

urlpatterns = [
    path("", index, name="home"),
    path("post/<int:post_id>", post, name="post"),
    path("add-post/", add_post, name="add_post"),
]
