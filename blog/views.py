from .forms import CommentForm
from django.views import generic, View
from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.db.models import Count
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogposts.html'
    paginate_by = 6


# def post_list(request):
#     posts = Post.objects.annotate(num_comments=Count('comments')).all()
#     return render(request, 'blog/blogposts.html', {'posts': posts})


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_expand.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )


# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.all()

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.author = request.user
#             comment.post = post
#             comment.save()
#             return redirect('post_detail', slug=post.slug)
#     else:
#         comment_form = CommentForm()

#    return render(request, 'blog/post_expand.html', {'post': post, 'comments':
#  comments, 'comment_form': comment_form})
