from django.db.models.fields import SlugField
from django.shortcuts import render, get_list_or_404
from .models import Post


def post_list(request):
    """
    List of posts.
    """
    posts = Post.published.all()
    return render(request, "blog/list.html")


def post_detail(request, year, month, day, post):
    """
    Post detail.
    """
    post = get_list_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "blog/detail.html", {"post": post})
