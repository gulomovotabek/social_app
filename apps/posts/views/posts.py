from django.db.models import Count
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from posts.models import Post
from posts.serializers import PostListSerializer, PostCreateSerializer, PostLikeSerializer


class PostViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_serializer_class(self):
        if self.action == "create":
            return PostCreateSerializer
        elif self.action == "list":
            return PostListSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        self.queryset = self.queryset.annotate(likes_count=Count('likes')).select_related('author')
        if self.action == 'list':
            return self.queryset.filter(author=self.request.user)
        elif self.action == 'liked':
            return self.queryset.filter(likes__action_by=self.request.user)
        return super().get_queryset()

    @action(["get"], False)
    def liked(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(["post"], True, serializer_class=PostLikeSerializer)
    def like(self, request, pk):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
