"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Authentication App (Login/Register/Logout PAGES)
    path('auth/', include('apps.authentication.web_urls')),

    # Session Auth (Browsable API Login)
    path('api/session-auth/', include('rest_framework.urls')),

    # Blog App (API)
    path('api/blog/', include('apps.blog.urls')),

    # Website (Templates)
    path('', include('apps.blog.web_urls')),

    # Authentication App (Login/Register)
    path('api/auth/', include('apps.authentication.urls')),
]
