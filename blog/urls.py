from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    #path("posts/<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("categories/<int:pk>/", views.CategoryView.as_view(), name="category"),
    path("tags/<int:pk>/", views.TagView.as_view(), name="tag"),
    path("api/posts/", views.posts),
    path("api/tags/", views.tags),
    path("api/categories/", views.cates),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    ]

