from django.shortcuts import get_object_or_404, render, get_list_or_404
from .models import Post
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    """
    List of posts.
    """
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, go to first page
        posts = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, go to last pae of results
        posts = paginator.page(paginator.num_pages)
    return render(request, "blog/index.html", {'page': page, "posts": posts, })


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
    post = get_object_or_404(
        Post,
        slug=post,
        status="published",
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, "blog/posts/detail.html",
                  {"post": post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})
