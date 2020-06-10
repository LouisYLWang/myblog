from rest_framework import serializers
from .models import Category, Post, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'name',
        ]


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer()
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'created_time',
            'excerpt',
            'category',
            'tags',
            'views',
            'img',
        ]

class PostRetrieveSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    toc = serializers.CharField()
    body_html = serializers.CharField()
 
    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body",
            "created_time",
            "modified_time",
            "excerpt",
            "views",
            "category",
            "tags",
            "toc",
            "body_html",
        ]
