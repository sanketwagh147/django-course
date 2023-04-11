"""simple_clone URL Configuration

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
from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, re_path

from simple_clone.views import HomePage, TestPage, ThanksPage

urlpatterns = [
    path("admin/", admin.site.urls),
    re_path("^$", HomePage.as_view(), name="home"),
    re_path(r"^accounts/", include("accounts.urls", namespace="accounts")),
    re_path(r"^accounts/", include("django.contrib.auth.urls")),  # uses inbuilt auth
    re_path(
        r"^test/", TestPage.as_view(template_name="test.html"), name="test"
    ),  # uses inbuilt auth
    re_path(r"^thanks/", ThanksPage.as_view(), name="thanks"),  # uses inbuilt auth
    re_path(r"^posts/", include("posts.urls", namespace="posts")),
    re_path(r"^groups/", include("groups.urls", namespace="groups")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [re_path(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
