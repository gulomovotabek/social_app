from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users import views


router = DefaultRouter()
# router.register('profile', views.ProfileViewSet, basename='profile')
profile_view = views.ProfileViewSet.as_view({
    'get': 'my_profile',
    'post': 'create',
    'put': 'update',
})
urlpatterns = [
    path("", include(router.urls)),
    path('profile', profile_view, name='profile'),
    path("login/", views.LoginView.as_view(), name="login"),
]
