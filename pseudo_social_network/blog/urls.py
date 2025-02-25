from django.urls import path, include
from django.contrib import admin
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.authtoken.views import obtain_auth_token
from .views import register
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def protected_resource(request):
    return JsonResponse({"message": "This is a protected resource."})

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/token/', include('rest_framework_simplejwt.urls')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', register, name='register'),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    path('protected-resource/', protected_resource),
]
