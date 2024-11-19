from rest_framework import serializers

from notifications.models import Notification
from posts.serializers import PostListSerializer
from users.serializers import RetrieveProfileSerializer


class NotificationSerializer(serializers.ModelSerializer):
    action_by = RetrieveProfileSerializer(read_only=True)
    post = PostListSerializer(read_only=True)

    class Meta:
        model = Notification
        fields = (
            'id',
            'type',
            'post',
            'action_by',
        )
