from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from notifications.models import Notification
from notifications.serializers import NotificationSerializer


class NotificationViewSet(ListModelMixin, GenericViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return self.queryset.filter(action_by=self.request.user)
