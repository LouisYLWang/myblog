from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from comments.forms import CommentForm
import markdown

# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
    'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    post.increase_views()

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                    'markdown.extensions.extra',
                                    'markdown.extensions.codehilite',
                                    'markdown.extensions.toc',
                                  ])
    form = CommentForm()
    review = len(post.comment_set.all())

    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list,
               'review':review

               }
    return render(request, 'blog/detail.html', context=context)
