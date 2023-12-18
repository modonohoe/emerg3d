from django.shortcuts import render
from django.db.models import Count
from .models import Post


def post_list(request):
    posts = Post.objects.annotate(num_comments=Count('comments')).all()
    return render(request, 'blog/blogposts.html', {'posts': posts})
