import os

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


def schema_view():
    return get_schema_view(
        openapi.Info(
            title="Social App",
            default_version="v1",
            description="Social App API",
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
