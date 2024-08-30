from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserProfileViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profile', UserProfileViewSet, basename='profile')

urlpatterns = [
    path('api1/auth/', include('dj_rest_auth.urls')),
    path('api1/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api1/userotoritation/', include(router.urls)),
    path('api1/userotoritation/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api1/userotoritation/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
