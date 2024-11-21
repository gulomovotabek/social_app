from django.contrib.auth import login
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.serializers import LoginSerializer


class LoginView(TokenObtainPairView):
    pass


class LoginWithSessionApiView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    @swagger_auto_schema(
        request_body=LoginSerializer,
    )
    def post(request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(User, username=serializer.validated_data['username'])
        login(request, user)
        return Response({"message": "success"})
