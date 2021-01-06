from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("tag/<slug:tag_slug>/", views.index, name="post_list_by_tag"),
    path("about/", views.about, name="about"),
    path("privacy/", views.privacy, name="privacy"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", views.post_detail, name="post_detail"),
]
