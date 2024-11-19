from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notifications.views.notifications import NotificationViewSet

router = DefaultRouter()
router.register('notifications', NotificationViewSet, basename='notifications')

urlpatterns = [
    path('', include(router.urls)),
]