from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.authtoken import views
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
]


# API Docs (Swagger, ReDoc)
schema_view = get_schema_view(
    openapi.Info(
        title="Admin Mailing Service API Documentation",
        default_version='v1',
        description="API documentation for Admin Mailing Service",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="grebenev-81@mail.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]