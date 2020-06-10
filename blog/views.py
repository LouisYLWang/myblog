from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from comments.forms import CommentForm
from .models import Category, Post, Tag
from .serializers import PostListSerializer, PostRetrieveSerializer, TagSerializer, CategorySerializer
import markdown

class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "post_list"
    paginate_by = 10

class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get("pk"))
        return super().get_queryset().filter(category=cate)

class TagView(IndexView):
    def get_queryset(self):
        t = get_object_or_404(Tag, pk=self.kwargs.get("pk"))
        return super().get_queryset().filter(tags=t)

class IndexPostListAPIView(ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]

'''
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        response = super(PostDetailView, self).get(request, *args, **kwargs)
        self.object.increase_views()
        return response
    
    def get_object(self, queryset=None):
        post = super().get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            TocExtension(slugify=slugify),
        ])
        post.body = md.convert(post.body)
 
        m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
        post.toc = m.group(1) if m is not None else ''
        return post
'''

class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()
    permission_classes = [AllowAny]
    serializer_class_table = {
        "list": PostListSerializer,
        "retrieve": PostRetrieveSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_class_table.get(
            self.action, super().get_serializer_class()
        )

posts = PostViewSet.as_view({'get': 'list'})

@api_view(http_method_names=["GET"])
def tags(request):
    tag_list = Tag.objects.all()
    serializer = TagSerializer(tag_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(http_method_names=["GET"])
def cates(request):
    cate_list = Category.objects.all()
    serializer = CategorySerializer(cate_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


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