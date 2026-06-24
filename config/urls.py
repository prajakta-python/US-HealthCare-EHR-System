# DRF — health-check API banavnyasathi
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Swagger (drf-spectacular) che ready-made views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from django.contrib import admin
from django.urls import path


# Aapli PAHILI API — health check
# "server jivant aahe ka?" he sangnari simple API
# ============================================================
@api_view(['GET'])                    # ही API fakt GET request gheते
@permission_classes([AllowAny])       # login nasla tarी chalel (public)
def health_check(request):
    return Response({                 # JSON answer pathavto
        "status": "ok",
        "service": "US Healthcare EHR API",
    })




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/health/',health_check,name='health-check'),
    path('api/schema/',SpectacularAPIView.as_view(),name='schema'),
    path('api/docs/',SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
]
