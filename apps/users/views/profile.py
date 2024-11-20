from rest_framework import permissions
from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
)
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.models import User
from users.serializers import (
    CreateProfileSerializer,
    RetrieveProfileSerializer,
    UpdateProfileSerializer,
)


class ProfileViewSet(CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CreateProfileSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.action == "create":
            return [permissions.AllowAny()]
        return super().get_permissions()

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateProfileSerializer
        elif self.action == ['update', 'partial_update']:
            return UpdateProfileSerializer
        return super().get_serializer_class()

    @staticmethod
    def my_profile(request):
        serializer = RetrieveProfileSerializer(request.user)
        return Response(serializer.data)
