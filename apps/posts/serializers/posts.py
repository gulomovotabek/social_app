from rest_framework import serializers

from notifications.models import Notification
from notifications.models.notifications import NotificationTypes
from posts.models import Post, Like
from users.serializers import RetrieveProfileSerializer


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'content',
        )

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class PostListSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)
    author = RetrieveProfileSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'content',
            'likes_count',
            'author',
        )


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
        )

    def update(self, instance, validated_data):
        Like.objects.create(post=instance, action_by=self.context['request'].user)
        Notification.objects.create(
            action_by=self.context['request'].user,
            post=instance,
            type=NotificationTypes.LIKE,
        )
        return instance
