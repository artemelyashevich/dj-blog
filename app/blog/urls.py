
from django.urls import path

from .views import index, post

urlpatterns = [
    path("", index, name="home"),
    path("post/<int:post_id>", post, name="post")
]
