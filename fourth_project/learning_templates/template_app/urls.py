from django.urls import re_path
from template_app import views

# Template tagging
app_name = "templates_app"


urlpatterns = [
    re_path(r"relative/$", views.relative, name="relative"),
    re_path(r"other/$", views.other, name="other"),
]
