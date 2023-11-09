from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

#from core_apps.users.views import CustomUserDetailsView

schema_view = get_schema_view(
    openapi.Info(
        title="Customer Manager",
        default_version="v1",
        description="API endpoints for Customer Manager API",
        contact=openapi.Contact(email="vinceotieno1@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
  
urlpatterns = [
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    path(settings.ADMIN_URL, admin.site.urls),
]

admin.site.site_header = "Customer Manager API Admin"

admin.site.site_title = "Customer Manager API Admin Portal"

admin.site.index_title = "Customer Manager API Portal"