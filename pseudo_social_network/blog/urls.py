from django.urls import path, include
from django.contrib import admin
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, register
from rest_framework.authtoken.views import obtain_auth_token
from .views import PublicationViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def protected_resource(request):
    return JsonResponse({"message": "This is a protected resource."})

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

router = DefaultRouter()
router.register(r'publications', PublicationViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include(router.urls)),
    path('api/register/', register, name='register'),
    path('api/token-auth/', obtain_auth_token, name='api_token_auth'),
    path('protected-resource/', protected_resource),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]
