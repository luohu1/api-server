from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular import views as schema_view
from rest_framework.routers import DefaultRouter

api_v1 = DefaultRouter()


urlpatterns = [
    re_path(r'^api/(?P<version>(v1|v2|v3))/', include(api_v1.urls)),
]

urlpatterns += [
    path('api/schema/', schema_view.SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', schema_view.SpectacularSwaggerView.as_view(), name='swagger-ui'),
    path('api/schema/redoc/', schema_view.SpectacularRedocView.as_view(), name='redoc'),
    path('admin/', admin.site.urls),
]
