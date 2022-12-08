"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    # This is to include authentication by rest frameowkr
    path('api-auth/', include('rest_framework.urls')),
    # This is to include authentication by dj_rest_auth package
    path('api/v1/dj-rest-auth/',include('dj_rest_auth.urls')),
    # This is to include all_auth authentication for registration
    path("api/v1/dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    # Following url's are for REDOC and SWAGGER API Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc",),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
# Endpoints for different tasks:
# Registration : http://127.0.0.1:8000/api/v1/dj-rest-auth/registration/
# Login : http://127.0.0.1:8000/api/v1/dj-rest-auth/login/
# Logout : http://127.0.0.1:8000/api/v1/dj-rest-auth/logout/
# Reset : http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset
# Reset confirm: http://127.0.0.1:8000/api/v1/dj-rest-auth/password/reset/confirm
