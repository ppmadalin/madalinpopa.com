from django.db.models.fields import SlugField
from django.shortcuts import render, get_list_or_404
from .models import Post


def index(request):
    """
    List of posts.
    """
    posts = Post.published.all()
    return render(request, "blog/index.html")


def about(request):
    """
    About page.
    """
    return render(request, "blog/about.html")


def privacy(request):
    """
    Privacy page.
    """
    return render(request, "blog/privacy.html")


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
    return render(request, "blog/posts/detail.html", {"post": post})