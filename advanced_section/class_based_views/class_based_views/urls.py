"""class_based_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from CBV_APP import views
from django.contrib import admin
from django.urls import include, path, re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    # re_path(r"^$", views.index),  # function based view
    # re_path(r"^$", views.CBView.as_view()),  # CBV version
    re_path(r"^$", views.IndexView.as_view()),  # CBV version
    path(r"CBV_APP/", include("CBV_APP.urls", namespace="CBV_APP")),  # CBV version
]
