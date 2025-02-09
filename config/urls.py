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

urlpatterns = [
    path('courses/', include('courses_app.urls')), # Link to courses_app urls.py | added in 2024/2/6
    path("unicorn/", include("django_unicorn.urls")), # Link to Django Unicorn Package urls.py | added in 2024/2/6
    path("admin/", admin.site.urls), # Django Default Admin Panel | added in 2024/2/6
]
