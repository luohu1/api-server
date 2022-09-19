from django.contrib import admin
from django.urls import path
from drf_spectacular import views as schema_view

urlpatterns = [
    path('api/schema/', schema_view.SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', schema_view.SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/schema/redoc/', schema_view.SpectacularRedocView.as_view(), name='redoc'),
    path('admin/', admin.site.urls),
]
